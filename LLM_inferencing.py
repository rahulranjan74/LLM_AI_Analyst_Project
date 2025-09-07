from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceEndpoint

def run_inferencing(input_ticker):

    # Load the text file
    loader = TextLoader(f'D:\PROJECTS\LLM based financial statement Analyser\{input_ticker}_10k_text.txt', encoding="utf-8")
    documents = loader.load()
    # Split the text into smaller chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    # Create embeddings for the text chunks
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # Create a vector store
    vector_store = FAISS.from_documents(texts, embeddings)


    import os
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
    # making the api call for Microsoft-Phi-3
    llm_llama3 =  HuggingFaceEndpoint(repo_id="meta-llama/Meta-Llama-3-8B-Instruct", temperature =0.7, model_kwargs={"max_length":10000, "min_length":1000})

    qa_chain = RetrievalQA.from_chain_type(llm = llm_llama3, retriever=vector_store.as_retriever())

    # Function to answer questions
    def answer_question(question):
        result = qa_chain({"query": question})
        return result["result"]

    # Example usage
    question = "With the information provided in the 10- filings give short but precise facts (including numbers) about the following : \n1.Companies stock Performance from the 10-k filings \n2.Analysis of Sales data \n3.Performance of Products \n4.Operating performance"
    answer = answer_question(question)

    return answer