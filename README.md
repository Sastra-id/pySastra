# pySastra

Lightweight Natural Language Processing for Indonesian Language.

# Design Plan

| Planned | Pipeline         | Description               |
|---------|------------------|---------------------------------------------|
| 🟠 | Language         | A text-processing pipeline. |
| 🟡 | Tokenizer        | Segment text, and create Doc objects with the discovered segment boundaries.|
| 🟠 | Lemmatizer       | Determine the base forms of words.|
| 🟡 | Morphology       | Assign linguistic features like lemmas, noun case, verb tense etc. based on the word and its part-of-speech tag.|
| 🟠 | Tagger           | Annotate part-of-speech tags on Doc objects.|
| 🔄 | DependencyParser | Annotate syntactic dependencies on Doc objects.|
| 🔄 | EntityRecognizer | Annotate named entities, e.g. persons or products, on Doc objects.|
| 🔄 | TextCategorizer  | Assign categories or labels to Doc objects.|
| 🔄 | Matcher          | Match sequences of tokens, based on pattern rules, similar to regular expressions.|
| 🔄 | PhraseMatcher    | Match sequences of tokens based on phrases.|
| 🔄 | EntityRuler      | Add entity spans to the Doc using token-based rules or exact phrase matches.|
| 🔄 | Sentencizer      | Implement custom sentence boundary detection logic that doesn’t require the dependency parse.|

🟢 Completed With Test
🟡 Completed
🟠 On Progress 
🔄 Planned

`reference : spaCy language pipeline`

