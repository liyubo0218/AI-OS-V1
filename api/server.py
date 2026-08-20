from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json


from mobile_gateway.gateway import MobileGateway

from core.context.context_manager import ContextManager
from core.brain.brain import Brain
from core.planner.planner import Planner
from core.orchestrator.orchestrator import Orchestrator

from execution.execution_engine import ExecutionEngine

from agents.agent_manager import AgentManager
from agents.demo_agent import DemoAgent

from memory.memory_manager import MemoryManager
from security.security_manager import SecurityManager


agent_manager = AgentManager()

agent_manager.register_agent(
    DemoAgent()
)


orchestrator = Orchestrator(
    ContextManager(),
    Brain(),
    Planner(),
    SecurityManager(),
    ExecutionEngine(),
    agent_manager,
    MemoryManager()
)


gateway = MobileGateway(
    orchestrator
)


class AIOSHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        if self.path == "/chat":

            length = int(
                self.headers["Content-Length"]
            )

            body = self.rfile.read(
                length
            )

            request = json.loads(
                body
            )


            result = gateway.handle_request(
                request
            )


            response = json.dumps(
                result,
                ensure_ascii=False
            )


            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.end_headers()


            self.wfile.write(
                response.encode("utf-8")
            )


def start_server():

    server = HTTPServer(
        ("localhost", 8000),
        AIOSHandler
    )


    print(
        "AI-OS API Server Running"
    )

    print(
        "POST http://localhost:8000/chat"
    )


    server.serve_forever()


if __name__ == "__main__":

    start_server()
