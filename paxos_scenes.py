from manim import *

class SingleProposer(Scene):
    def construct(self):
        title = Text("Scenario 1: Single Proposer (No Conflict)", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Nodes
        proposer = Circle(radius=0.6, color=BLUE).shift(LEFT * 5)
        proposer_txt = Text("Proposer P1", font_size=28).next_to(proposer, DOWN)
        acceptors = VGroup(*[
            Circle(radius=0.6, color=GREEN).shift(RIGHT * (i * 2)) for i in [-1, 0, 1]
        ]).shift(RIGHT)
        acc_txts = VGroup(*[
            Text(f"A{i+1}", font_size=28).move_to(acc.get_center()) for i, acc in enumerate(acceptors)
        ])
        learner = Circle(radius=0.6, color=YELLOW).shift(DOWN * 3)
        learner_txt = Text("Learner", font_size=28).next_to(learner, DOWN)

        # Draw nodes
        self.play(Create(proposer), Write(proposer_txt))
        self.play(Create(acceptors), Write(acc_txts))
        self.play(Create(learner), Write(learner_txt))
        self.wait(3)

        # Prepare phase
        for acc in acceptors:
            arr = Arrow(proposer.get_right(), acc.get_left(), buff=0.2)
            lbl = Text("Prepare: #1", font_size=24).next_to(arr, UP)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        # Promise phase
        for acc in acceptors:
            arr = Arrow(acc.get_left(), proposer.get_right(), buff=0.2, color=GRAY)
            lbl = Text("Promise", font_size=24).next_to(arr, DOWN)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        # Accept phase
        for acc in acceptors:
            arr = Arrow(proposer.get_right(), acc.get_left(), buff=0.2, color=BLUE)
            lbl = Text("Accept: v=42", font_size=24).next_to(arr, UP)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        # Accepted -> Learner
        for acc in acceptors:
            arr = Arrow(acc.get_bottom(), learner.get_top(), buff=0.2, color=ORANGE)
            lbl = Text("Accepted", font_size=24).next_to(arr, LEFT)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        result = Text("Value 42 chosen", font_size=32, color=YELLOW).next_to(learner, DOWN)
        self.play(Write(result))
        self.wait(10)


class ConflictProposers(Scene):
    def construct(self):
        title = Text("Scenario 2: Two Proposers Competing", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Nodes
        p1 = Circle(radius=0.6, color=BLUE).shift(LEFT * 5 + DOWN * 1)
        p2 = Circle(radius=0.6, color=RED).shift(LEFT * 3 + UP * 1.5)
        self.play(Create(p1), Write(Text("P1 (#1)", font_size=28).next_to(p1, DOWN)))
        self.play(Create(p2), Write(Text("P2 (#2)", font_size=28).next_to(p2, UP)))

        acceptors = VGroup(*[
            Circle(radius=0.6, color=GREEN).shift(RIGHT * (i * 2)) for i in [-1, 0, 1]
        ]).shift(RIGHT)
        acc_txts = VGroup(*[
            Text(f"A{i+1}", font_size=28).move_to(acc.get_center()) for i, acc in enumerate(acceptors)
        ])
        self.play(Create(acceptors), Write(acc_txts))
        self.wait(3)

        # P1 Prepare
        for acc in acceptors:
            arr = Arrow(p1.get_right(), acc.get_left(), buff=0.2, color=BLUE)
            lbl = Text("P1: Prepare #1", font_size=24).next_to(arr, UP)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        # P2 Prepare
        for acc in acceptors:
            arr = Arrow(p2.get_bottom(), acc.get_top(), buff=0.2, color=RED)
            lbl = Text("P2: Prepare #2", font_size=24).next_to(arr, RIGHT)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        # Acceptors promise to P2
        for acc in acceptors:
            arr = Arrow(acc.get_top(), p2.get_bottom(), buff=0.2, color=RED)
            lbl = Text("Promise", font_size=24).next_to(arr, LEFT)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        # P2 Accept
        for acc in acceptors:
            arr = Arrow(p2.get_bottom(), acc.get_top(), buff=0.2, color=RED)
            lbl = Text("Accept: v=84", font_size=24).next_to(arr, UP)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        result = Text("P2 wins: Value 84 chosen", font_size=32, color=RED).shift(DOWN * 3)
        self.play(Write(result))
        self.wait(10)


class FailureRecovery(Scene):
    def construct(self):
        title = Text("Scenario 3: Proposer Failure & Recovery", font_size=40).to_edge(UP)
        self.play(Write(title))

        # Nodes
        p1 = Circle(radius=0.6, color=BLUE).shift(LEFT * 5)
        p2 = Circle(radius=0.6, color=RED).shift(RIGHT * 5)
        self.play(Create(p1), Write(Text("P1 (#1)", font_size=28).next_to(p1, DOWN)))
        self.play(Create(p2), Write(Text("P2 (#2)", font_size=28).next_to(p2, DOWN)))

        acceptors = VGroup(*[
            Circle(radius=0.6, color=GREEN).shift(RIGHT * (i * 2)) for i in [-1, 0, 1]
        ])
        acc_txts = VGroup(*[
            Text(f"A{i+1}", font_size=28).move_to(acc.get_center()) for i, acc in enumerate(acceptors)
        ])
        self.play(Create(acceptors), Write(acc_txts))
        self.wait(3)

        # P1 Prepare
        for acc in acceptors:
            arr = Arrow(p1.get_right(), acc.get_left(), buff=0.2, color=BLUE)
            lbl = Text("P1: Prepare #1", font_size=24).next_to(arr, UP)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        # P1 failure
        self.play(FadeOut(p1), run_time=1)
        self.wait(5)

        # P2 Prepare
        for acc in acceptors:
            arr = Arrow(p2.get_left(), acc.get_right(), buff=0.2, color=RED)
            lbl = Text("P2: Prepare #2", font_size=24).next_to(arr, RIGHT)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        # P2 Accept
        for acc in acceptors:
            arr = Arrow(p2.get_left(), acc.get_right(), buff=0.2, color=RED)
            lbl = Text("P2: Accept v=99", font_size=24).next_to(arr, DOWN)
            self.play(GrowArrow(arr), Write(lbl), run_time=3)
        self.wait(5)

        result = Text("P2 recovers: Value 99 chosen", font_size=32, color=RED).shift(DOWN * 3)
        self.play(Write(result))
        self.wait(10)


class Discussion(Scene):
    def construct(self):
        title = Text("Discussion: Paxos Guarantees", font_size=44).to_edge(UP)
        self.play(Write(title))
        self.wait(3)

        lines = [
            "• Safety: Only one value is ever chosen",
            "• Liveness: Progress when majority respond",
            "• Resolves proposer conflicts by numbering",
            "• Tolerates failures and recovers safely"
        ]
        bullets = VGroup(*[
            Text(line, font_size=30).next_to(title, DOWN, buff=0.8).shift(DOWN * i * 0.6)
            for i, line in enumerate(lines)
        ])
        for b in bullets:
            self.play(Write(b), run_time=3)
            self.wait(5)

        thanks = Text("Thanks for watching!", font_size=36, color=YELLOW).to_edge(DOWN)
        self.play(Write(thanks))
        self.wait(3)
