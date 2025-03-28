# Proposal

## What will (likely) be the title of your project?

ShareNote-AMA-Bot

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

I am going to create a RAG model that can take in notes submitted by students and later use those to answer questions.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

This is a part of a large project I am working. I am going to create a MVP model for this class. The system access notes from a S3 bucket (text or basic document), chunk and embed the content, store it in a vector database, and expose an API endpoint that can be queried with a question. The backend will retrieve relevant note chunks using semantic similarity then pass them along with the question to OpenAI api, and return the generated answer. The goal is to build a well-documented, working RAG pipeline with a REST API interface.

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

Functional RAG pipeline with local document ingestion, embedding, storage in vector DB, and retrieval.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

RAG pipeline + REST API built using fastapi or flask

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

Adding authentication, and a fully deployed API on AWS.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

I need to do some research on how to parse and chunk uploaded documents effectively and store embeddings for fast search.
