"""
Swarm of multi modal autonomous agents for manufacturing!
---------------------------------------------------------    
Health Security agent: Agent that monitors the health of working conditions: input image of factory output: health safety index 0.0 - 1.0 being the highest
Quality Control agent: Agent that monitors the quality of the product: input image of product output: quality index 0.0 - 1.0 being the highest
Productivity agent: Agent that monitors the productivity of the factory: input image of factory output: productivity index 0.0 - 1.0 being the highest
Safety agent: Agent that monitors the safety of the factory: input image of factory output: safety index 0.0 - 1.0 being the highest
Security agent: Agent that monitors the security of the factory: input image of factory output: security index 0.0 - 1.0 being the highest
Sustainability agent: Agent that monitors the sustainability of the factory: input image of factory output: sustainability index 0.0 - 1.0 being the highest
Efficiency agent: Agent that monitors the efficiency of the factory: input image of factory output: efficiency index 0.0 - 1.0 being the highest    


Flow:
health security agent -> quality control agent -> productivity agent -> safety agent -> security agent -> sustainability agent -> efficiency agent 
"""
from swarms.structs import Flow, SequentialWorkflow
from swarms.models import GPT4VisionAPI
from swarms.prompts.multi_modal_autonomous_instruction_prompt import (
    MULTI_MODAL_AUTO_AGENT_SYSTEM_PROMPT_1,
)


llm = GPT4VisionAPI()

assembly_line = "assembly_line.jpg"
red_robots = "red_robots.jpg"
robots = "robots.jpg"
tesla_assembly_line = "tesla_assembly.jpg"


# Define detailed prompts for each agent
tasks = {
    "health_safety": (
        "Analyze the factory's working environment for health safety. Focus on"
        " cleanliness, ventilation, spacing between workstations, and personal"
        " protective equipment availability."
    ),
    "productivity": (
        "Review the factory's workflow efficiency, machine utilization, and"
        " employee engagement. Identify operational delays or bottlenecks."
    ),
    "safety": (
        "Analyze the factory's safety measures, including fire exits, safety"
        " signage, and emergency response equipment."
    ),
    "security": (
        "Evaluate the factory's security systems, entry/exit controls, and"
        " potential vulnerabilities."
    ),
    "sustainability": (
        "Inspect the factory's sustainability practices, including waste"
        " management, energy usage, and eco-friendly processes."
    ),
    "efficiency": (
        "Assess the manufacturing process's efficiency, considering the layout,"
        " logistics, and automation level."
    ),
}


# Define prompts for each agent
health_safety_prompt = tasks["health_safety"]
productivity_prompt = tasks["productivity"]
safety_prompt = tasks["safety"]
security_prompt = tasks["security"]
sustainability_prompt = tasks["sustainability"]
efficiency_prompt = tasks["efficiency"]


# Health security agent
health_security_agent = Flow(
    llm=llm,
    sop=MULTI_MODAL_AUTO_AGENT_SYSTEM_PROMPT_1 + health_safety_prompt,
    max_loops=2,
)

# Quality control agent
quality_control_agent = Flow(
    llm=llm,
    sop=MULTI_MODAL_AUTO_AGENT_SYSTEM_PROMPT_1,
    max_loops=2,
)

# Quality control agent
productivity_check_agent = Flow(
    llm=llm,
    sop=MULTI_MODAL_AUTO_AGENT_SYSTEM_PROMPT_1 + productivity_prompt,
    max_loops=2,
)

# Security agent
security_check_agent = Flow(
    llm=llm,
    sop=MULTI_MODAL_AUTO_AGENT_SYSTEM_PROMPT_1 + security_prompt,
    max_loops=2,
)

# Efficiency agent
efficiency_check_agent = Flow(
    llm=llm,
    sop=MULTI_MODAL_AUTO_AGENT_SYSTEM_PROMPT_1 + efficiency_prompt,
    max_loops=2,
)


# Sequential workflow
workflow = SequentialWorkflow(
    max_loops=4,
    name="Swarm of multi modal autonomous agents for manufacturing!",
    description="Swarm of multi modal autonomous agents for manufacturing!",
)

# Add the first task to the health_security_agent
health_check = workflow.add(
    health_security_agent,
    "Analyze the safety of this factory",
    robots
)

# Add the third task to the productivity_check_agent
productivity_check = workflow.add(
    productivity_check_agent, health_check, assembly_line
)

# Add the fourth task to the security_check_agent
security_check = workflow.add(
    security_check_agent, productivity_check, red_robots
)

# Add the fifth task to the efficiency_check_agent
efficiency_check = workflow.add(
    efficiency_check_agent, security_check, tesla_assembly_line
)


# Run the workflow
workflow.run()