# 🎯 LangGraph Basics: Build Stateful AI Workflows Progressively

## 📚 What is LangGraph?

LangGraph is a framework for building **stateful, multi-step AI workflows** using graphs. Unlike simple LLM chains, LangGraph gives you explicit control over how data flows through your application, enabling complex decision-making, loops, and conditional routing.

## 🏗️ What You'll Build

A progressive series of graphs that demonstrates:
1. **Basic Imports** - Foundation setup with StateGraph, END, TypedDict
2. **Node Functions** - State transformation basics without graphs
3. **Connected Edges** - Your first complete graph
4. **Multi-step Flows** - Document processing workflow
5. **Conditional Routing** - Dynamic decision-making
6. **Calculator Tool** - First LLM integration
7. **Research Agent** - Complete assistant with calculator + web search

## 📋 Lab Structure (7 Progressive Tasks)

### Task 1: Understanding Imports 📦
**File:** `task_1_understanding_imports.py` (44 lines)

**Concept:** Master the essential imports needed for LangGraph

**What You'll Do:**
- Import StateGraph and END from langgraph.graph
- Import TypedDict from typing
- Define your first State class with messages list
- Understand the building blocks WITHOUT execution

**3 TODOs:**
- **Line 10:** Import modules: `from langgraph.graph import StateGraph, END`
- **Line 14:** Import TypedDict: `from typing import TypedDict`
- **Line 19:** Define messages field: `messages: list`

**Key Learning:** StateGraph creates workflows, END marks completion, State holds data

---

### Task 2: Creating Nodes ⚙️
**File:** `task_2_creating_nodes.py` (61 lines)

**Concept:** Learn that nodes are functions that transform state

**What You'll Do:**
- Create greet_node that generates a greeting
- Create enhance_node that adds decorations
- Test nodes manually WITHOUT a graph
- See how nodes return partial state updates

**3 TODOs:**
- **Line 20:** Return greeting: `return {"greeting": greeting}`
- **Line 28:** Return enhanced greeting: `return {"greeting": enhanced}`

**Key Learning:** Nodes are functions that take state and return PARTIAL updates

---

### Task 3: Connecting Edges 🔗
**File:** `task_3_connecting_edges.py` (70 lines)

**Concept:** Build your first complete graph with edges

**What You'll Do:**
- Create your first StateGraph
- Add nodes using add_node
- Connect nodes with add_edge
- Set entry point and compile
- Run your first workflow!

**3 TODOs:**
- **Line 33:** Create StateGraph: `workflow = StateGraph(State)`
- **Line 38:** Add enhance node: `workflow.add_node("enhance", enhance_node)`
- **Line 43:** Connect edges: `workflow.add_edge("greet", "enhance")`

**Key Learning:** StateGraph + add_node + add_edge = Complete workflow!

---

### Task 4: Complete Flow 🎯
**File:** `task_4_complete_flow.py` (86 lines)

**Concept:** Multi-step document processing workflow

**What You'll Do:**
- Build a 3-step workflow: outline → draft → review
- See state accumulation across multiple nodes
- Each node builds on previous results
- Complete multi-step processing

**3 TODOs:**
- **Line 37:** Return final: `return {"final": final}`
- **Line 48:** Add review node: `workflow.add_node("review", review_node)`
- **Line 54:** Connect to review: `workflow.add_edge("draft", "review")`

**Key Learning:** Multi-node workflows process data in stages with state accumulation

---

### Task 5: Conditional Routing 🔀
**File:** `task_5_conditional_routing.py` (115 lines)

**Concept:** Dynamic path selection based on state

**What You'll Do:**
- Analyze query length to determine routing
- Create router function that returns node names
- Route to quick_response or detailed_response
- Master add_conditional_edges

**3 TODOs:**
- **Line 27:** Router condition: `if state["query_length"] == "short":`
- **Line 57:** Set entry point: `workflow.set_entry_point("analyze")`
- **Line 66:** Map routing: `"detailed": "detailed"`

**Key Learning:** Router examines state → Returns node name → Graph routes dynamically

---

### Task 6: Calculator Tool 🧮
**File:** `task_6_calculator_tool.py` (124 lines)

**Concept:** First LLM integration as a calculator

**What You'll Do:**
- Classify queries as math or non-math
- Route to calculator_node for math queries
- Use LLM to solve calculations
- Handle non-math queries gracefully

**3 TODOs:**
- **Line 40:** Router condition: `if state["is_math"]:`
- **Line 51:** Return result: `return {"result": f"Answer: {answer}"}`
- **Line 76:** Map routing: `"calculator": "calculator"`

**Key Learning:** Tools are just nodes with specific functions, LLM can act as calculator

---

### Task 7: Research Agent 🔬
**File:** `task_7_research_agent.py` (146 lines)

**Concept:** Complete assistant with multiple tools

**What You'll Do:**
- Initialize DuckDuckGo search
- Classify queries as math or search
- Route to calculator for math
- Route to web search for information
- Build a complete research assistant!

**3 TODOs:**
- **Line 28:** Initialize search: `ddgs = DDGS()`
- **Line 59:** Return result: `return {"result": f"Calculation result: {answer}"}`
- **Line 67:** Search web: `results = ddgs.text(state["query"], max_results=2)`

**Key Learning:** Smart routing between multiple tools based on query type

## 🚦 Getting Started

### 1. Environment Setup
```bash
# Activate virtual environment
cd /root && source /root/venv/bin/activate

# Install dependencies
pip install langgraph langchain langchain-openai duckduckgo-search

# Verify environment
python3 /root/code/verify_environment.py
```

### 2. Required Packages
- `langgraph` - Stateful graph framework
- `langchain` - Core LLM abstractions
- `langchain-openai` - OpenAI integration
- `duckduckgo-search` - Free web search (no API key needed!)

### 3. Environment Variables
Pre-configured in the container:
- `OPENAI_API_BASE` - Proxy endpoint for LLM access
- `OPENAI_API_KEY` - Authentication
- `OPENAI_MODEL` - Default model (gpt-4.1-mini)

## 🎯 Expected Outcomes

By completing this lab, you'll understand:

1. **Foundation Setup**
   - Essential imports for LangGraph
   - State definition with TypedDict
   - Building blocks before execution

2. **Nodes as State Transformers**
   - Functions that take state and return partial updates
   - No side effects - pure state transformations
   - Testing nodes without graphs

3. **Graphs as Orchestrators**
   - StateGraph manages node execution order
   - Fixed edges for linear flow
   - Entry points and compilation

4. **Multi-Step Workflows**
   - State accumulation across nodes
   - Each node building on previous results
   - Complex document processing

5. **Conditional Routing**
   - Router functions examine state
   - Dynamic path selection
   - Mapping router outputs to nodes

6. **Tool Integration**
   - LLM as a calculator
   - Query classification
   - Smart tool routing

7. **Complete Research Agent**
   - Multiple tool integration
   - Web search capabilities
   - Intelligent query routing

## 🆘 Troubleshooting

### Common Issues:

**Import Error:**
```bash
# Solution: Reinstall packages
pip install langgraph langchain langchain-openai duckduckgo-search
```

**State Type Error:**
```python
# Problem: Missing field in State
class State(TypedDict):
    field1: str
    # field2: str  # ← Forgot to add this!

# Solution: Add all required fields
```

**Routing Error:**
```python
# Problem: Router output doesn't match node names
# Solution: Ensure router returns exact node names
```

**DuckDuckGo Rate Limit:**
```python
# DuckDuckGo may rate-limit requests
# Solution: Wait 10 seconds and retry
```

## 🏆 Challenge Extensions

Once you complete all 7 tasks, try these extensions:

1. **Add More Tools**
   - Weather API for weather queries
   - News API for current events
   - Database lookup for structured data

2. **Improve Classification**
   - Use LLM to classify queries (more accurate)
   - Add confidence scores to routing
   - Handle edge cases gracefully

3. **Add Validation**
   - Grade search results for relevance
   - Loop back if results are poor
   - Implement fallback strategies

## 📖 Your Learning Journey

```
START → Imports → Nodes → Edges → Flows → Routing → Calculator → Research Agent → COMPLETE!
  ↓        ↓        ↓       ↓       ↓        ↓          ↓            ↓
Learn   Create   Connect  Multi   Dynamic   LLM      Multiple    You're a
Basics  Functions Graph    Step   Decisions  Tool     Tools      LangGraph Pro!
```

## 🔥 Next Steps

**Advanced LangGraph Patterns:**
- 🧠 Memory systems for conversation history
- 👤 Human-in-the-Loop workflows
- 🔄 Self-improvement loops with validation
- 🤖 Multi-agent collaboration
- 🚀 Production deployment patterns

## 📚 Additional Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangGraph Tutorials](https://github.com/langchain-ai/langgraph/tree/main/examples)
- [LangChain Documentation](https://python.langchain.com/docs/)
