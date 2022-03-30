import os


HEADER = """version: '3.3'  # version of compose format

services:"""

TEMPLATE = """
  {}-service:
    build: ./{} # path is relative to docker-compose.yml location
    hostname: {}-service{}
    networks:
      sample:
        aliases:
          - {}-service"""
  
PORT_MAPPING = """
    ports:
      - 5050:5050  # host:container"""

FOOTER = """
networks:
  sample:
"""

def get_services():
    services_sorted = sorted(list(os.walk('microservices/'))[0][1])
    services_sorted.remove('landing')
    return services_sorted

""" 
To use:
  - Add all microservice apps in `microservices/
  - In project root directory, Run `python3 tools/gen_compose.py > <docker-compose-path>`
"""
if __name__ == "__main__":
    print(HEADER)
    services = get_services()
    print(TEMPLATE.format("landing", "landing", "landing", PORT_MAPPING, "landing"))
    for service_name in services:
        print(TEMPLATE.format(service_name, service_name, service_name, "", service_name))
    print(FOOTER)