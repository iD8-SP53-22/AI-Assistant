from langchain import PromptTemplate
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.vectorstores import FAISS 
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as cl

DB_FAISS_PATH = "vectorstores/db_faiss"
version = "1.0.0"

custom_prompt_template = """Use the following pieces of information to answer the users questions, if you don't know the answer, please just say that you do not know the answer, do not try to make up an answer

Context: {context}
Question: {question}

Only returns the correct and helpful answer below and nothing else
Helpful answer:
"""


class Model:
    def set_custom_prompt():
        """
        Prompt Template for QA retrieval for each vector stores
        """

        prompt = PromptTemplate(template = custom_prompt_template, input_variables = ["context", "question"])

        return prompt

    def load_llm():
        llm = CTransformers(
            model = "llama-2-7b-chat.ggmlv3.q8_0.bin",
            model_type = 'llama',
            max_new_tokens = 2048,
            temperature =  0.5
        )

        return llm

    def retrieval_qa_chain(llm, prompt, db):
        qa_chain = RetrievalQA.from_chain_type(
            llm = llm,
            chain_type = "stuff",
            retriever = db.as_retriever(search_lwargs={'k': 2}),
            return_source_documents = True,
            chain_type_kwargs = {'prompt': prompt}
        )

        return qa_chain

    def qa_bot():
        embeddings = FastEmbedEmbeddings()

        db = FAISS.load_local(DB_FAISS_PATH, embeddings)
        llm = Model.load_llm()
        qa_prompt = Model.set_custom_prompt()
        qa = Model.retrieval_qa_chain(llm, qa_prompt, db)

        return qa

    def final_result(query):
        qa_result = Model.qa_bot()
        response = qa_result({'query' : query})

        return response

"""The below code is unnecessary for our purposes, but serves as a good way of testing our chatbot with an easy to understand user interface created using"""
## Chainlit ####
@cl.on_chat_start
async def start():
    chain = Model.qa_bot()
    msg = cl.Message(content= "Starting Bot")
    await msg.send()
    msg.content = f"Welcome to test version {version} of the AI Assistant, enter query"
    await msg.update()
    cl.user_session.set("chain", chain)

@cl.on_message
async def main(message):
    chain = cl.user_session.get("chain")
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer = True, answer_prefix_tokens = ["FINAL", "ANSWER"]
    )
    cb.answer_reached = True
    res = await chain.acall(message.content, callbacks = [cb])
    answer = res["result"]
    sources = res["source_documents"]

    # if sources:
    #     answer += f"\nSources:" + str(sources)
    # else:
    #     answer += f"\n no sources found"
    
    # await cl.Message(content=answer).send()