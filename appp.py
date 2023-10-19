import autogen

config_list = [
    {
        "api_type": "open_ai",
        "api_base":"http://localhost:1234/v1",
        "api_key": "NULL"
    }
]

llm_config={
    "request_timeout": 600,
    "seed": 44,                     # for caching and reproducibility
    "config_list": config_list,     # which models to use
    "temperature": 0,              
}

agent_assistant = autogen.AssistantAgent(
    name="agent_assistant",
    llm_config=llm_config,
)
 #user agent
agent_proxy = autogen.UserProxyAgent(
    name="agent_proxy",
    human_input_mode="NEVER",           # NEVER, TERMINATE, or ALWAYS 
                                            # TERMINATE - human input needed when assistant sends TERMINATE 
    max_consecutive_auto_reply=10,
    code_execution_config={
        "work_dir": "agent_output",     # path for file output of program
        "use_docker": False,            
    },
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
                      Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

agent_proxy.initiate_chat(
    agent_assistant,
    message="""I need you to write a python script that will print the first 10 prime numbers of numbers
    from 1 to 100.
    """,
)

#agent_proxy.initiate_chat(
    #agent_assistant,
    #message="""I need you to write a python script that will create a streamlit application that converts
    #text to speech.
   # """,
#)