# Fist Agent Exmaple:

# Loads variables from a .env file into the process environment
from dotenv import load_dotenv
# NOTE: `os` is imported but never used
import os
# PromptTemplate: a reusable prompt string with {placeholders} to fill in at run time
from langchain_core.prompts import PromptTemplate
# ChatOpenAI: LangChain wrapper around OpenAI's chat models (e.g. gpt-5)
from langchain_openai import ChatOpenAI


# Read .env now so the OpenAI client can find OPENAI_API_KEY in the environment
load_dotenv()



def main():
    print("Hello from langchain-course!")
    # Source text about a person; the model will summarize this
    information = """
    Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is an industrialist, technologist, and former public official who is the chief executive officer (CEO) and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire (in terms of US dollars) in June 2026; as of October 2026, Forbes estimates his net worth to be $1.1 trillion.

    Born into the wealthy Musk family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded Zip2, a web software company. Following its sale in 1999, he co-founded X.com, an e-commerce payment system that merged with Confinity in March 2000 to form PayPal. Musk also became an American citizen in 2002.

    In 2002, Musk founded and became CEO and chief engineer of SpaceX, a space technology company. Musk joined Tesla as an angel investor in 2004 and became its CEO and product architect in 2008. In 2015, Musk co-founded OpenAI to advance artificial intelligence (AI) research, but later left; his growing discontent with the organization's direction and leadership in the AI boom in the 2020s led him to establish xAI, which became a subsidiary of SpaceX in 2026. In 2022, he acquired Twitter, a social networking service, and made significant changes, including rebranding it as X in 2023. His other businesses include Neuralink, a neurotechnology company that he co-founded in 2016, and the Boring Company, a tunneling company that he founded in 2017. In November 2025, Tesla approved a pay package worth $1 trillion for Musk, which he is to receive over 10 years if certain milestones are met, such as achieving a market capitalization of $8.5 trillion. Musk became the first US-dollar trillionaire upon the initial public offering of SpaceX in June 2026, though a SpaceX stock collapse brought him under the threshold by the next month.
    """

    # The prompt text; {information} is replaced with the text above when the chain runs
    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them

        """

    # Wrap the template string so LangChain can fill in its variables
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # Chat model; temperature is left at the default (gpt-5 may reject temperature=0)
    llm = ChatOpenAI(model="gpt-5")
    # `|` pipes the prompt's output into the model (LangChain Expression Language)
    chain = summary_prompt_template | llm

    # Run the chain, supplying a value for each placeholder in the prompt
    response = chain.invoke(input={"information": information})
    # ChatOpenAI returns a message object; .content holds the text
    print(response.content)

if __name__ == "__main__":
    main()
