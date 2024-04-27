from utils.messageUtil import MessageUtil
from service.llmService import LLMService

class MessageService:
    def __init__(self):
        self.messageUtil = MessageUtil()
        self.llmService = LLMService()

    def processMessage(self, message):
        if self.messageUtil.isBankSms(message=message):
            return self.llmService.runLLM(message=message)
        else:
            return None