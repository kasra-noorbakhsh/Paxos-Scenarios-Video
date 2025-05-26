from manim import *

class PaxosAnimation(Scene):
    def construct(self):
        def create_acceptors():
            acceptors = VGroup(*[
                Circle(radius=0.5, color=GREEN).shift(RIGHT * (i * 2.5 - 2.5)) for i in range(3)
            ])
            acc_txts = VGroup(*[
                Text(f"A{i+1}", font_size=24).move_to(acc.get_center()) for i, acc in enumerate(acceptors)
            ])
            return acceptors, acc_txts

        title1 = Text("Scenario 1: Single Proposer (No Conflict)", font_size=36).to_edge(UP, buff=0.7)
        self.play(Write(title1))
        self.wait(1)

        proposer = Circle(radius=0.5, color=BLUE).shift(LEFT * 4)
        proposer_txt = Text("Proposer P1", font_size=24).next_to(proposer, DOWN, buff=0.4)
        acceptors, acc_txts = create_acceptors()
        learner = Circle(radius=0.5, color=YELLOW).shift(DOWN * 3.5)
        learner_txt = Text("Learner", font_size=24).next_to(learner, DOWN, buff=0.4)

        self.play(Create(proposer), Write(proposer_txt))
        self.play(Create(acceptors), Write(acc_txts))
        self.play(Create(learner), Write(learner_txt))
        self.wait(1)

        prepare_arrows = VGroup()
        prepare_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(proposer.get_right(), acc.get_left(), buff=0.3)
            lbl = Text("Prepare: #1", font_size=18).next_to(arr, UP, buff=0.3).shift(LEFT * 0.2 * i)
            prepare_arrows.add(arr)
            prepare_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(1)

        promise_arrows = VGroup()
        promise_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(acc.get_left(), proposer.get_right(), buff=0.3, color=GRAY)
            lbl = Text("Promise", font_size=18).next_to(arr, DOWN, buff=0.3).shift(RIGHT * 0.2 * i)
            promise_arrows.add(arr)
            promise_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(1)

        accept_arrows = VGroup()
        accept_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(proposer.get_right(), acc.get_left(), buff=0.3, color=BLUE)
            lbl = Text("Accept: v=42", font_size=18).next_to(arr, UP, buff=0.3).shift(RIGHT * 0.2 * i)
            accept_arrows.add(arr)
            accept_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(1)

        learn_arrows = VGroup()
        learn_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(acc.get_bottom(), learner.get_top(), buff=0.3, color=ORANGE)
            lbl = Text("Accepted", font_size=18).next_to(arr, LEFT, buff=0.3).shift(DOWN * 0.2 * i)
            learn_arrows.add(arr)
            learn_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(1)

        result1 = Text("Value 42 chosen", font_size=28, color=YELLOW).next_to(learner, DOWN, buff=0.6)
        self.play(Write(result1))
        self.wait(1.5)

        self.play(
            FadeOut(title1), FadeOut(proposer), FadeOut(proposer_txt),
            FadeOut(acceptors), FadeOut(acc_txts), FadeOut(learner), FadeOut(learner_txt),
            FadeOut(prepare_arrows), FadeOut(prepare_labels),
            FadeOut(promise_arrows), FadeOut(promise_labels),
            FadeOut(accept_arrows), FadeOut(accept_labels),
            FadeOut(learn_arrows), FadeOut(learn_labels),
            FadeOut(result1)
        )
        self.wait(0.5)

        title2 = Text("Scenario 2: Two Proposers Competing", font_size=36).to_edge(UP, buff=0.7)
        self.play(Write(title2))
        self.wait(0.5)

        p1 = Circle(radius=0.5, color=BLUE).shift(LEFT * 4 + DOWN * 1)
        p2 = Circle(radius=0.5, color=RED).shift(LEFT * 4 + UP * 1)
        p1_txt = Text("P1 (#1)", font_size=24).next_to(p1, DOWN, buff=0.4)
        p2_txt = Text("P2 (#2)", font_size=24).next_to(p2, UP, buff=0.4)
        acceptors, acc_txts = create_acceptors()

        self.play(Create(p1), Write(p1_txt))
        self.play(Create(p2), Write(p2_txt))
        self.play(Create(acceptors), Write(acc_txts))
        self.wait(0.5)

        p1_prepare_arrows = VGroup()
        p1_prepare_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(p1.get_right(), acc.get_left(), buff=0.3, color=BLUE)
            lbl = Text("P1: Prepare #1", font_size=18).next_to(arr, UP, buff=0.3).shift(LEFT * 0.2 * i)
            p1_prepare_arrows.add(arr)
            p1_prepare_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(0.5)

        p2_prepare_arrows = VGroup()
        p2_prepare_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(p2.get_right(), acc.get_left(), buff=0.3, color=RED)
            lbl = Text("P2: Prepare #2", font_size=18).next_to(arr, DOWN, buff=0.3).shift(RIGHT * 0.2 * i)
            p2_prepare_arrows.add(arr)
            p2_prepare_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(0.5)

        promise_arrows = VGroup()
        promise_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(acc.get_left(), p2.get_right(), buff=0.3, color=RED)
            lbl = Text("Promise", font_size=18).next_to(arr, DOWN, buff=0.3).shift(LEFT * 0.2 * i)
            promise_arrows.add(arr)
            promise_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(0.5)

        accept_arrows = VGroup()
        accept_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(p2.get_right(), acc.get_left(), buff=0.3, color=RED)
            lbl = Text("Accept: v=84", font_size=18).next_to(arr, UP, buff=0.3).shift(RIGHT * 0.2 * i)
            accept_arrows.add(arr)
            accept_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(0.5)

        result2 = Text("P2 wins: Value 84 chosen", font_size=28, color=RED).shift(DOWN * 3.5)
        self.play(Write(result2))
        self.wait(1.5)

        self.play(
            FadeOut(title2), FadeOut(p1), FadeOut(p2), FadeOut(p1_txt), FadeOut(p2_txt),
            FadeOut(acceptors), FadeOut(acc_txts),
            FadeOut(p1_prepare_arrows), FadeOut(p1_prepare_labels),
            FadeOut(p2_prepare_arrows), FadeOut(p2_prepare_labels),
            FadeOut(promise_arrows), FadeOut(promise_labels),
            FadeOut(accept_arrows), FadeOut(accept_labels),
            FadeOut(result2)
        )
        self.wait(0.5)

        title3 = Text("Scenario 3: Proposer Failure & Recovery", font_size=36).to_edge(UP, buff=0.7)
        self.play(Write(title3))
        self.wait(0.5)

        p1 = Circle(radius=0.5, color=BLUE).shift(LEFT * 4)
        p2 = Circle(radius=0.5, color=RED).shift(RIGHT * 4)
        p1_txt = Text("P1 (#1)", font_size=24).next_to(p1, DOWN, buff=0.4)
        p2_txt = Text("P2 (#2)", font_size=24).next_to(p2, DOWN, buff=0.4)
        acceptors, acc_txts = create_acceptors()

        self.play(Create(p1), Write(p1_txt))
        self.play(Create(p2), Write(p2_txt))
        self.play(Create(acceptors), Write(acc_txts))
        self.wait(0.5)

        p1_prepare_arrows = VGroup()
        p1_prepare_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(p1.get_right(), acc.get_left(), buff=0.3, color=BLUE)
            lbl = Text("P1: Prepare #1", font_size=18).next_to(arr, UP, buff=0.3).shift(LEFT * 0.2 * i)
            p1_prepare_arrows.add(arr)
            p1_prepare_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(0.5)

        self.play(FadeOut(p1), FadeOut(p1_txt), run_time=0.8)
        self.wait(0.5)

        p2_prepare_arrows = VGroup()
        p2_prepare_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(p2.get_left(), acc.get_right(), buff=0.3, color=RED)
            lbl = Text("P2: Prepare #2", font_size=18).next_to(arr, DOWN, buff=0.3).shift(RIGHT * 0.2 * i)
            p2_prepare_arrows.add(arr)
            p2_prepare_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(0.5)

        accept_arrows = VGroup()
        accept_labels = VGroup()
        for i, acc in enumerate(acceptors):
            arr = Arrow(p2.get_left(), acc.get_right(), buff=0.3, color=RED)
            lbl = Text("P2: Accept v=99", font_size=18).next_to(arr, UP, buff=0.3).shift(LEFT * 0.2 * i)
            accept_arrows.add(arr)
            accept_labels.add(lbl)
            self.play(GrowArrow(arr), Write(lbl), run_time=0.8)
        self.wait(0.5)

        result3 = Text("P2 recovers: Value 99 chosen", font_size=28, color=RED).shift(DOWN * 3.5)
        self.play(Write(result3))
        self.wait(1.5)

        self.play(
            FadeOut(title3), FadeOut(p2), FadeOut(p2_txt),
            FadeOut(acceptors), FadeOut(acc_txts),
            FadeOut(p1_prepare_arrows), FadeOut(p1_prepare_labels),
            FadeOut(p2_prepare_arrows), FadeOut(p2_prepare_labels),
            FadeOut(accept_arrows), FadeOut(accept_labels),
            FadeOut(result3)
        )
        self.wait(0.5)

        title4 = Text("Discussion: Paxos Guarantees", font_size=36).to_edge(UP, buff=0.7)
        self.play(Write(title4))
        self.wait(0.5)

        lines = [
            "• Safety: Only one value is ever chosen",
            "• Liveness: Progress when majority respond",
            "• Resolves proposer conflicts by numbering",
            "• Tolerates failures and recovers safely"
        ]
        bullets = VGroup(*[
            Text(line, font_size=28).to_edge(LEFT, buff=1).shift(DOWN * (i * 1.0 + 1))
            for i, line in enumerate(lines)
        ])
        for b in bullets:
            self.play(Write(b), run_time=0.8)
            self.wait(0.5)

        thanks = Text("Thanks for watching!", font_size=32, color=YELLOW).to_edge(DOWN, buff=0.7)
        self.play(Write(thanks))
        self.wait(1.5)

        self.play(FadeOut(title4), FadeOut(bullets), FadeOut(thanks))
        self.wait(0.5)