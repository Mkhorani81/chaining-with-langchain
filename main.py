from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

#import os
#api_key = 'default value'
#os.environ['OPENAI_API_KEY'] = api_key

information = "What are the diffrences between iphone 13 and iphone 14"

if __name__ == "__main__":
    print("Hello LangChain!")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0,
                     model_name="gpt-3.5-turbo")  # temperture will decide how creative the language model will be

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))
