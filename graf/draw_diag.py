from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file('quiz', '../math_quiz.py')
cfg.build_visual('quiz', 'png')