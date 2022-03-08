# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from typing import Iterator
import time
from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        # self.model = torch.load("./weights.pth")

    def predict(
        self,
        num_iterations: int = Input(description="Number of iterations", default=600),
        sleep_time: int = Input(default=10),
    ) -> Iterator[str]:
        start_time = time.time()
        for i in range(num_iterations):
            text = f"Iteration: {(i + 1)}; time: {time.time() - start_time:.0f}"
            print(text)
            yield text
            time.sleep(sleep_time)
