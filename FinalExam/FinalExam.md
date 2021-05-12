# Final Exam CS475 Artificial Intelligence I

Ziad Arafat
May 11 2021

### 1

#### a.

- Satisfiable?
  - **Yes**
    - Because there exists a model of A,B,C,D where the formula results true.
- Valid?
  - **No**
    - Because there exists a model of A,B,C,D where the fomula results false
- Unsatisfiable?
  - **No**
    - Because not all the models of A,B,C,D cause the the formula to result in a false. 

| A | B | C | D |$(((A ∨ B) ∨ (¬A → (¬B ∧ ¬D))) ∧ (C → (B ∨ D)))$|
|:-:|:-:|:-:|:-:|:----------------------------------------------:|
| F | F | F | F | T                                              |
| F | F | F | T | F                                              |
| F | F | T | F | F                                              |
| F | F | T | T | F                                              |
| F | T | F | F | T                                              |
| F | T | F | T | T                                              |
| F | T | T | F | T                                              |
| F | T | T | T | T                                              |
| T | F | F | F | T                                              |
| T | F | F | T | T                                              |
| T | F | T | F | F                                              |
| T | F | T | T | T                                              |
| T | T | F | F | T                                              |
| T | T | F | T | T                                              |
| T | T | T | F | T                                              |
| T | T | T | T | T                                              |


#### b.

$$((((A \lor B) \rightarrow C) \lor (\neg A \rightarrow (\neg B \land \neg D))) \land (C \rightarrow (B \lor D)))$$


$$((((A ∨ B) → C) ∨ (¬A → (¬B ∧ ¬D))) ∧ (C → (B ∨ D)))$$
- Convert conditionals according to conditional law $p → q = ¬p ∨ q$ 
$$(((¬(A ∨ B) ∨ C) ∨ (¬¬A ∨ (¬B ∧ ¬D))) ∧ (¬C ∨ (B ∨ D)))$$
- distrubite negation with demorgan's law
$$((((¬A ∧ ¬B) ∨ C) ∨ (¬¬A ∨ (¬B ∧ ¬D))) ∧ (¬C ∨ (B ∨ D)))$$
- cancel out double negation $¬¬A$
$$((((¬A ∧ ¬B) ∨ C) ∨ (A ∨ (¬B ∧ ¬D))) ∧ (¬C ∨ (B ∨ D)))$$
- Distribute $(¬A ∧ ¬B) ∨ C$
$$(((C ∨ ¬A) ∧ (C ∨ ¬B) ∨ (A ∨ (¬B ∧ ¬D))) ∧ (¬C ∨ (B ∨ D)))$$
- Distribute $A ∨ (¬B ∧ ¬D)$
$$(((C ∨ ¬A) ∧ (C ∨ ¬B) ∨ (A∨¬B) ∧ (A∨¬D)) ∧ (¬C ∨ B ∨ D))$$
- Distribute $((C∨¬A) ∧ (C∨¬B)) ∨ ((A∨¬B) ∧ (A∨¬D))$
$$((C∨¬A)∨(A∨¬B)) ∧ ((C∨¬A)∨(A∨¬D)) ∧ ((C∨¬B)∨(A∨¬B)) ∧ ((C∨¬B)∨(A∨¬D)) ∧ (¬C∨B∨D)$$


<!-- 
((A\/¬B)/\(A\/¬D)\/(C\/¬B))/\((A\/¬B)/\(A\/¬D)\/(C\/¬A))/\(¬C\/B\/D)

(A\/¬B)/\(A\/¬D)\/(C\/¬B)/\(A\/¬B)/\(A\/¬D)\/(C\/¬A)/\(¬C\/B\/D)

((C\/¬B)\/(A\/¬B)) /\ ((C\/¬B)\/(A\/¬D)) /\ ((A\/¬B)/\(A\/¬D)\/(C\/¬A)) /\ (¬C\/B\/D)

((C\/¬B)\/(A\/¬B))/\((C\/¬B)\/(A\/¬D))/\ ((C\/¬A)\/(A\/¬B)) /\ ((C\/¬A)\/(A\/¬D)) /\ (¬C \/ B \/ D)

((C\/¬B)\/(A\/¬B))/\((C\/¬B)\/(A\/¬D))/\ ((C\/¬A)\/(A\/¬B)) /\ ((C\/¬A)\/(A\/¬D)) /\ (¬C \/ B \/ D) -->