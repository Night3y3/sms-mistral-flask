from dotenv import load_dotenv, dotenv_values
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.utils.function_calling import convert_to_openai_tool
import os
from schema.expenseSchema import ExpenseSchema

class LLMService:
    def __init__(self):
        load_dotenv()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                # it is he llm system prompt
                (
                    "system",
                    "You are an expert extraction algorithm. "
                    "Only extract relevant information from the text. "
                    "If you do not know the value of an attribute asked to extract, "
                    "return null for the attribute's value.",
                ),
                # it is the human prompt where text is the placeholder/input
                ("human","{text}")
            ]
        )
        self.apiKey = os.getenv("MISTRAL_API_KEY")
        self.llm = ChatMistralAI(api_key=self.apiKey, model_name="mistral-large-latest", temperature=0)
        self.runnable = self.prompt | self.llm
    def runLLM(self, message):
        return self.runnable.invoke({"text":message}) # this will find the placeholder text and replace it with the message