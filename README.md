# The Abstraction and Reasoning Corpus (ARC)

This repository contains the ARC task data, as well as a browser-based interface for humans to try their hand at solving the tasks manually.

*"ARC can be seen as a general artificial intelligence benchmark, as a program synthesis benchmark, or as a psychometric intelligence test. It is targeted at both humans and artificially intelligent systems that aim at emulating a human-like form of general fluid intelligence."*

A complete description of the dataset, its goals, and its underlying logic, can be found in: [The Measure of Intelligence](https://arxiv.org/abs/1911.01547).

As a reminder, a test-taker is said to solve a task when, upon seeing the task for the first time, they are able to produce the correct output grid for *all* test inputs in the task (this includes picking the dimensions of the output grid). For each test input, the test-taker is allowed 3 trials (this holds for all test-takers, either humans or AI).


## Task file format

The `data` directory contains two subdirectories:

- `data/training`: contains the task files for training (400 tasks). Use these to prototype your algorithm or to train your algorithm to acquire ARC-relevant cognitive priors.
- `data/evaluation`: contains the task files for evaluation (400 tasks). Use these to evaluate your final algorithm. To ensure fair evaluation results, do not leak information from the evaluation set into your algorithm (e.g. by looking at the evaluation tasks yourself during development, or by repeatedly modifying an algorithm while using its evaluation score as feedback).

The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

- `"train"`: demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
- `"test"`: test input/output pairs. It is a list of "pairs" (typically 1 pair).

A "pair" is a dictionary with two fields:

- `"input"`: the input "grid" for the pair.
- `"output"`: the output "grid" for the pair.

A "grid" is a rectangular matrix (list of lists) of integers between 0 and 9 (inclusive). The smallest possible grid size is 1x1 and the largest is 30x30.

When looking at a task, a test-taker has access to inputs & outputs of the demonstration pairs, plus the input(s) of the test pair(s). The goal is to construct the output grid(s) corresponding to the test input grid(s), using 3 trials for each test input. "Constructing the output grid" involves picking the height and width of the output grid, then filling each cell in the grid with a symbol (integer between 0 and 9, which are visualized as colors). Only *exact* solutions (all cells match the expected answer) can be said to be correct.


## Usage of the testing interface

The testing interface is located at `apps/testing_interface.html`. Open it in a web browser (Chrome recommended). It will prompt you to select a task JSON file.

After loading a task, you will enter the test space, which looks like this:

![test space](https://arc-benchmark.s3.amazonaws.com/figs/arc_test_space.png)

On the left, you will see the input/output pairs demonstrating the nature of the task. In the middle, you will see the current test input grid. On the right, you will see the controls you can use to construct the corresponding output grid.

You have access to the following tools:

### Grid controls

- Resize: input a grid size (e.g. "10x20" or "4x4") and click "Resize". This preserves existing grid content (in the top left corner).
- Copy from input: copy the input grid to the output grid. This is useful for tasks where the output consists of some modification of the input.
- Reset grid: fill the grid with 0s.

### Symbol controls

- Edit: select a color (symbol) from the color picking bar, then click on a cell to set its color.
- Select: click and drag on either the output grid or the input grid to select cells.
    - After selecting cells on the output grid, you can select a color from the color picking to set the color of the selected cells. This is useful to draw solid rectangles or lines.
    - After selecting cells on either the input grid or the output grid, you can press C to copy their content. After copying, you can select a cell on the output grid and press "V" to paste the copied content. You should select the cell in the top left corner of the zone you want to paste into.
- Floodfill: click on a cell from the output grid to color all connected cells to the selected color. "Connected cells" are contiguous cells with the same color.

### Answer validation

When your output grid is ready, click the green "Submit!" button to check your answer. We do not enforce the 3-trials rule.

After you've obtained the correct answer for the current test input grid, you can switch to the next test input grid for the task using the "Next test input" button (if there is any available; most tasks only have one test input).

When you're done with a task, use the "load task" button to open a new task.

#################################################################################################################

Team: Thomas Sebastian (Student No: 21250103) and David Power (Student No: 21249194)

ARC Puzzles solved: 5582e5ca / d511f180 / f8b3ba0a / 22eb0ac0 / e3497940 / c3f564a4 / f8ff0b80 / c8f0f002 / d631b094 
ARC Puzzle part-solved: d0f5fe59

Running manual_solve.py executes the puzzle solution functions where the input, output arrays and a boolean True or False is printed to the console. 

Discussion:

The ARC (Abstract Reasoning Corpus) is a benchmark towards measuring general intelligence of both humans and computer agents. Theories of intelligence vary, not only in computer science, but also within psychology, neuroscience and even between cultures. Three well known Intelligence theories from psychology and psychometrics are those of Spearman's g Theory, The Horn-Cattell Theory and Sternberg's Triarchic Theory. Having an understanding of what intelligence actually is and how it can be measured is crucial in computer science for those that wish to build intelligent systems. Spearman refers to 'g' the general factor as a general ability or general intelligence that can be applied to various intellectual acts or tasks after learning them on specific tasks. The Horn-Cattell Theory is concerned with fluid and crystallized abilities of intelligence. Fluid intelligence is the pure form of intelligence and crystallized intelligence is integrated through culture. One of the goals of Chollet with ARC is to measure fluid intelligence. Fluid intelligence can be thought of the ability to solve problems which is not dependant on prior knowledge, education or training. Sternberg’s Triarchic Theory is divided into three parts, the componential subtheory, the experiential subtheory and contextual subtheory. The componential subtheory is concerned with the behaviour involved in solving problems, such as performance and knowledge-acquisition and processing new information. The experiential subtheory is concerned with solving novel problems. The contextual subtheory is concerned with adaption to the environment. Intelligence is a complex concept, both in psychology and computer science, a collective definition remains elusive, however examining several theories gives one an underpinning of what intelligence is and how it may be measured. There are several definitions of AI in computer science such as “AI is the science of marking machines capable of performing tasks that would require intelligence if done by humans” by Minsky (1968). This poses a problem as it infers that the AI evaluation of the whether the machine has performed the task well is carried out by humans. Also, this leads to an anomaly in the fact for all the successes of AI, the systems built are solving problems without actually featuring intelligence [ref 1-5]. 

AI to date has had many successes in several challenging environments, and now outperforms humans in chess, Go and some older Atari games, amongst others. However, these successes are built on the fact that the tasks used for training were either identical or extremely similar to the ones used for testing. The agent may not have been exposed to the test but often drawn from the same distribution. This is turn led to superhuman performance on very specific tasks, but agents that cannot generalise. Therefore, these agents cannot be considered intelligent in same terms as a human’s ability to adapt and generalise. For agents to be considered truly intelligent then they must be able to adapt, function and generalise across a wide number of environments and unexpected situations. This is the challenge brought forth by the ARC. A new area of research looking at training and testing animal like artificial cognition for general AI ability, where AI environments and agents are built and designed similar to radial maze environments and rodent, where the AI agent must use spatial reasoning, collect food, move objects, maximise rewards and so forth is an interesting concept. However, clearly more work is needed as the AI agents performed at 40% versus their human counterparts at 100%. The Obstacle Tower is an AI generalisation challenge in vision, control and planning on a gaming platform. The agent must solve both low-level control and high-level planning problems in addition to learning from the screen pixel output and sparse reward signal. The intelligence of the agent is based on its performance and ability of unseen instances of the environment.  The AI agent performed poorly, even worse than the worst performing human across all metrics. More work in AI generalisation is needed, rather than AI solving individual problems. These improvements will have impact across all AI domains from robotics to navigation and planning. When measuring an agent that is designed for a very specific purpose, we are actually measuring the programmer’s ability to solve the problem and not actual intelligence. More work is also needed in evaluating AI agents, moving from task-oriented measurement to ability-orientated measurement. Development must be directed towards intelligent and human-like AI agents, ARC is designed to be a measurement of human-like form of general fluid intelligence, where a fair general intelligence comparison between AI agents and human counterparts can be performed [ref 1-5]. 
The tasks undertaken were a mix of both easy and medium complex tasks. Several of the solutions are task specific, however several also will generalise also to very similar tasks. The lofty goals and aspirations of generalisation was not attempted on this iteration of attempts to solve the ARC problem. 

References:
1. Challot, F. (2019). On the Measure of Intelligence. ArXiv:1911.01547v2
2. Cocodia, E. (2014). Cultural Perceptions of Human Intelligence. Journal of Intelligence. 2: pp180-196
3. Beyret, B., Hernandez-Orallo, J., Cheke, L., Halina, M., Shanahan, M. & Crosby, m. (2019). The Animal-AI Environment: Training and Testing Animal-Like Artificial Cognition. ArXix: 1909.07483v2
4. Juliani, A., Khaifa, A., Berges, V., Harper, J., Teng, E., Henry, H., Cresi, A., Togelius, J. & Lange, D. (2019). Obstacle Tower: A Generalization in Vision, Control and Planning. Proceedings of the 28th International Joint Conference On AI (IJCAI-19). 
5. Hernandez-Orallo, J. (2017). Evaluation in artificial Intelligence: from task-orientated to ability-orientated measurement. Artificial Intelligence Review. 48: pp 397-447 doi:10.1007/s10462-016-9505-7




