from manim import *

class FadingText(Scene):
    def construct(self):
        # Create a Text object
        text = Text("Jay Hanuman", font_size=100)

        # Fade in the text
        self.play(FadeIn(text))

        # Wait for a moment
        self.wait(1)

        # Fade out the text
        self.play(FadeIn(text))

        self.wait(1)

if __name__ == "__main__":
    scene = FadingText()
    scene.render()