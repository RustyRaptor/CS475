# CS 475 Logic

### 1.

###### I do acknowlege that if we account for all the vocabulary it would increase the number of models in which the result is false and true. But I initially counted those models as redundant as those parts of the vocabulary are not incorporated in the formula. 

#### a.

- There are 3 models
  - If we count the redundant vocabulary there are 6 

| A | B | C | $((A \land B) \lor (B \land C))$ |
|:-:|:-:|:-:|:-------------------:|
| F | F | F |          F          |
| F | F | T |          F          |
| F | T | F |          F          |
| F | T | T |          T          |
| T | F | F |          F          |
| T | F | T |          F          |
| T | T | F |          T          |
| T | T | T |          T          |

#### b.

- There are 3 models
  - If we count the redundant vocabulary there are 12

| A | B | $(A \lor B)$ |
|:-:|:-:|:-------:|
| F | F |    F    |
| F | T |    T    |
| T | F |    T    |
| T | T |    T    |

#### c.

- There are 4 models
        - If we count the redundant vocabulary there are 8


| A | B | C | $(A \Leftrightarrow (B \Leftrightarrow C))$ |
|:--:|:--:|:--:|:-------------:|
| F | F | F |       F       |
| F | F | T |       T       |
| F | T | F |       T       |
| F | T | T |       F       |
| T | F | F |       T       |
| T | F | T |       F       |
| T | T | F |       F       |
| T | T | T |       T       |

#### d.

- There is only 1 model
        - If we count the redundant vocabulary there are 16

| D | $D$ |
|:-:|:-:|
| F | F |
| T | T |


### 2.

#### a.

- Valid: Yes
        - All models result in True
- Satisfiable: Yes
        - At least one model results in True

| smoke | $(smoke \Rightarrow smoke)$ |
|:-----:|:---------------:|
|   F   |        T        |
|   T   |        T        |

#### b.

- Valid: No
        - Not all models result in True
- Satisfiable: Yes
        - At least one model results in True

| fire | smoke | $((smoke \Rightarrow fire) \Rightarrow (\neg smoke \Rightarrow \neg fire))$ |
|:----:|:-----:|:-----------------------------------:|
|   F  |   F   |                  T                  |
|   F  |   T   |                  T                  |
|   T  |   F   |                  F                  |
|   T  |   T   |                  T                  |

#### c.

- Valid: Yes
        - All models result in True
- Satisfiable: Yes
        - At least one model results in True

| fire | heat | smoke | $(((smoke  \land  heat)  \Rightarrow  fire)  \Leftrightarrow  ((smoke  \Rightarrow  fire) \lor (heat  \Rightarrow  fire)))$|
|:----:|:----:|:-----:|:------------------------------------------------------------:|
|   F  |   F  |   F   |                               T                              |
|   F  |   F  |   T   |                               T                              |
|   F  |   T  |   F   |                               T                              |
|   F  |   T  |   T   |                               T                              |
|   T  |   F  |   F   |                               T                              |
|   T  |   F  |   T   |                               T                              |
|   T  |   T  |   F   |                               T                              |
|   T  |   T  |   T   |                               T                              |

### 3.

#### a.

$$((A \land B) \lor (B \land C)) \Rightarrow (D \land E) $$

$$\neg ((A \land B) \lor (B \land C)) \lor (D \land E) $$

$$ (\neg( A \land B) \land \neg (B \land C)) \lor (D \land E) $$

$$ (( \neg A \lor \neg B) \land  (\neg B \lor \neg C)) \lor (D \land E) $$

$$(D \land E) \lor (( \neg A \lor \neg B) \land  (\neg B \lor \neg C))$$

$$((D \land E) \lor ( \neg A \lor \neg B)) \land  ((D \land E) \lor (\neg B \lor \neg C))$$


$$(  ( \neg A \lor \neg B)\lor (D \land E)) \land  ( (\neg B \lor \neg C)\lor (D \land E))$$

$$( \neg A \lor \neg B \lor D) \land  ( \neg A \lor \neg B \lor E) \land  (\neg B \lor \neg C \lor D) \land (\neg B \lor \neg C \lor E)$$


#### b. 

$$((A \lor B) \land (B \lor C)) \Rightarrow (D \lor E) $$

$$\neg ((A \lor B) \land (B \lor C)) \lor (D \lor E) $$

$$ (\neg(A \lor B) \lor \neg (B \lor C)) \lor (D \lor E) $$

$$ ((\neg A \land \neg B) \lor (\neg B \land \neg C)) \lor (D \lor E) $$

$$ ((\neg A \land \neg B) \lor (\neg B \land \neg C)) \lor (D \lor E) $$

$$ ((\neg B \land \neg A) \lor (\neg B \land \neg C)) \lor (D \lor E) $$

$$ (\neg B \land (\neg A \lor \neg C)) \lor (D \lor E) $$

$$ (D \lor E) \lor (\neg B \land (\neg A \lor \neg C))   $$

$$ (D \lor E \lor \neg B) \land (D \lor E \lor \neg A \lor \neg C) $$ 


### 4.

$$ ((P \Rightarrow Q) \land (L \land M \Rightarrow P) \land (L \land B \Rightarrow M) \land (A \land P \Rightarrow L) \land (A \land B \Rightarrow L) \land A \land B) \Rightarrow Q $$

$$ ((\neg P \lor Q) \land (\neg (L \land M) \lor P) \land (\neg (L \land B) \lor M) \land (\neg (A \land P) \lor L) \land (\neg(A \land B) \lor L) \land A \land B) \Rightarrow Q $$

$$ ((\neg P \lor Q) \land (\neg L \lor \neg M \lor P) \land (\neg L \lor \neg B \lor M) \land (\neg A \lor \neg P) \lor L) \land (\neg A \lor \neg B \lor L) \land A \land B) \Rightarrow Q $$

$$ ((\neg P \lor Q) \land (\neg L \lor \neg M \lor P) \land (\neg L \lor \neg B \lor M) \land ( \neg P) \lor L) \land (  \neg B \lor L) \land B) \Rightarrow Q $$

$$ ((\neg P \lor Q) \land (\neg L \lor \neg M \lor P) \land (\neg L \lor M) \land ( \neg P) \lor L) \land  L) \Rightarrow Q $$

$$ ((\neg P \lor Q) \land (\neg M \lor P) \land  M \land  \neg P ) \Rightarrow Q $$

$$ ((\neg P \lor Q) \land P \land  \neg P ) \Rightarrow Q $$

$$ Q \Rightarrow Q $$

- $Q \Rightarrow Q$ is valid 
- Therefore $KB$ entails $Q$