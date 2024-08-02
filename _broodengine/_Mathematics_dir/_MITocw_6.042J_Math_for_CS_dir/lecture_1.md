### MIT 6.042J: Mathematics for Computer Science
### Lecture 1: Introduction and Proofs

**Date:** [Insert Date]  
**Instructor:** Tom Leighton

#### 1. Introduction to Discrete Mathematics

**1.1 What is Discrete Mathematics?**
- Discrete mathematics is the study of mathematical structures that are fundamentally discrete, not requiring the notion of continuity.
- It includes topics such as logic, set theory, combinatorics, graph theory, and discrete probability.

**1.2 Importance in Computer Science**
- Discrete mathematics provides the theoretical foundation for many aspects of computer science, including algorithms, data structures, cryptography, and software engineering.
- It helps in developing rigorous proofs and understanding the complexity of algorithms.

**1.3 Course Overview**
- The course covers fundamental concepts and proof techniques, with an emphasis on problem-solving and logical reasoning.
- Key topics include:
  - **Logic and Proofs:** Understanding logical statements and constructing valid proofs.
  - **Set Theory:** Basics of sets, subsets, set operations, and their properties.
  - **Functions and Relations:** Definitions, types, properties, and applications.
  - **Counting and Combinatorics:** Techniques for counting, permutations, combinations, and the principles of inclusion-exclusion.
  - **Graph Theory:** Basics of graphs, trees, and their applications.
  - **Number Theory:** Properties of integers, divisibility, primes, and modular arithmetic.
  - **Probability:** Basic concepts of probability, conditional probability, and their applications.

#### 2. Fundamental Concepts

**2.1 Sets**
- A set is a collection of distinct objects, considered as an object in its own right.
- Notation: `A = {1, 2, 3}` indicates that set `A` contains elements 1, 2, and 3.
- Basic operations include union (`∪`), intersection (`∩`), difference (`-`), and complement (`A^c`).

**2.2 Logic and Propositions**
- A proposition is a declarative sentence that is either true or false.
- Logical connectives: AND (`∧`), OR (`∨`), NOT (`¬`), IMPLIES (`→`), and IF AND ONLY IF (`↔`).
- Truth tables are used to determine the truth values of logical expressions.

**2.3 Functions**
- A function `f` from set `A` to set `B` is a relation that assigns each element `a ∈ A` exactly one element `b ∈ B`.
- Notation: `f: A → B`.
- Types of functions include injective (one-to-one), surjective (onto), and bijective (both).

**2.4 Relations**
- A relation on a set `A` is a subset of `A × A`.
- Properties: Reflexive, Symmetric, Transitive, Equivalence Relations, Partial Orders.

#### 3. Proof Techniques

**3.1 Direct Proof**
- Prove that a statement `P → Q` is true by assuming `P` and showing `Q`.

**3.2 Proof by Contradiction**
- Assume the negation of what you want to prove, show that this assumption leads to a contradiction, thus proving the original statement.

**3.3 Proof by Induction**
- **Base Case:** Prove the statement for the initial value (usually `n = 0` or `n = 1`).
- **Inductive Step:** Assume the statement holds for some arbitrary value `k` (inductive hypothesis), and then prove it holds for `k + 1`.

#### 4. Examples and Exercises

**4.1 Example: Proving a Basic Property**
- **Proposition:** The sum of two even numbers is even.
- **Proof:** Let `a = 2m` and `b = 2n` where `m` and `n` are integers. Then `a + b = 2m + 2n = 2(m+n)`, which is even.

**4.2 Example: Using Induction**
- **Proposition:** For any natural number `n`, the sum of the first `n` positive integers is `\frac{n(n+1)}{2}`.
- **Proof:**
  - **Base Case:** For `n = 1`, `1 = \frac{1(1+1)}{2} = 1`.
  - **Inductive Step:** Assume it holds for `k`, i.e., `1 + 2 + ... + k = \frac{k(k+1)}{2}`. Then for `k+1`, `1 + 2 + ... + k + (k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}`.

**4.3 Exercises:**
- Prove that the product of two odd numbers is odd.
- Show that the union of two sets `A` and `B` is commutative, i.e., `A ∪ B = B ∪ A`.
- Prove by induction that for all `n ∈ ℕ`, `2^n ≥ n+1`.

#### 5. Conclusion and Wrap-Up

**5.1 Summary of Key Points**
- Discrete mathematics is crucial for computer science.
- Understanding sets, logic, functions, and relations is foundational.
- Various proof techniques are essential for establishing mathematical truths.

**5.2 Looking Ahead**
- Future lectures will delve deeper into each of these topics.
- Homework and reading assignments will reinforce the concepts covered.

For more detailed course materials, including lecture notes, assignments, and video lectures, you can visit the [MIT OpenCourseWare page for Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/pages/readings/).
