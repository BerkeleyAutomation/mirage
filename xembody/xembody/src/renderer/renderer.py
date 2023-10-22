from abc import ABC, abstractmethod
from xembody.src.renderer.render_result import RenderResult

class Renderer(ABC):

    @abstractmethod
    def initialize(self) -> None:
        """
        Initializes the appropriate camera in the simulator.
        """
        pass

    @abstractmethod
    def render_current_view(self) -> RenderResult:
        """
        Renders the current view of the robot in a particular state.
        :return: RenderResult: The result of the rendering.
        """
        pass