# Ledger part J3 — Correlated voters, coincident failures, and heterogeneity

Checked 2026-10-03. Every work was read in full text except Ladha (1992), which could not be opened. Sources of record are the SEP archive page, the NeurIPS proceedings pages (1994, 2023, 2024), Crossref DOI records, arXiv abs pages, and the OpenReview search API. Full texts came from the following:
- the SEP entry (current and Spring 2023 archive copies, identical in body text);
- NeurIPS proceedings PDFs (Krogh–Vedelsby, Chen et al., Toups et al.);
- the free Springer PDF (Kuncheva–Whitaker);
- NASA NTRS, for Eckhardt–Lee's precursor NASA TM-86369;
- the authors' own manuscript of Knight–Leveson from Nancy Leveson's MIT site. The host timed out, so its Internet Archive capture was read;
- the scanned publisher PDF of Vaupel et al. on Vaupel's MPIDR publication page, read as page images;
- arXiv v3 (Brown et al.).

Retraction checks used the Crossref `query.bibliographic` API (rows=3) and the arXiv abs pages. Blocked and not bypassed:
- JSTOR (Ladha) showed a "Client Challenge".
- IEEE Xplore (both IEEE TSE papers) returned an empty bot-protection response.
- Duke University Press (Vaupel) showed a Cloudflare challenge.
- DBLP showed an Anubis bot check.
- The MIT Press page returned 403.
- The Semantic Scholar API was rate-limited.

One quote per source, under 15 words. Everything else is paraphrased with locations. Numbers marked "our arithmetic" are not printed in the source. `J3_voting.bib` (10 entries) passed a test run of bibtex with the paper's IEEEtran.bst: 10 bibitems, 0 warnings.

Works a reviewer may also name that were not carded or verified here: Littlewood and Miller (1989, IEEE TSE 15(12):1596–1614; Crossref metadata only), which generalizes the Eckhardt–Lee model; Dietrich and Spiekermann (2013a), the primary source of the Competence-Sensitive Jury Theorem that the SEP entry reports; Ladha (1993, Social Choice and Welfare 10(1)), a different Ladha paper on interchangeable voters.

---

### dietrich2023jury
- Source of record: https://plato.stanford.edu/archives/spr2023/entries/jury-theorems/ (Stanford Encyclopedia of Philosophy, Spring 2023 Edition, Edward N. Zalta and Uri Nodelman, eds.). The SEP's citation page, https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=jury-theorems, says the latest version is to be cited via this archive edition. The entry was first published 17 Nov 2021 and last modified 18 Feb 2023 (minor correction). Access: full text (https://plato.stanford.edu/entries/jury-theorems/ and the Spring 2023 archive copy; read Secs. 1.1, 2.1–2.6, 3.1–3.4 and the bibliography).
- Retraction: not applicable to Crossref, since SEP entries have no DOI and the Crossref query returned unrelated items. The SEP revision history lists only minor corrections (Summer 2022, Spring 2023), with no withdrawal.
- Card:
  - Setting: a survey of jury theorems. Each is a binary choice with one correct alternative, decided by majority vote under probabilistic premises about voters' competence and independence.
  - What it establishes:
    - Sec. 2.1 states Condorcet's theorem. Under Unconditional Independence and Unconditional Competence (every voter right with the same probability, above 1/2), the probability of a correct majority increases with (odd) group size and converges to 1.
    - Sec. 2.2: common causes make votes probabilistically dependent even when voters do not influence one another. Examples are shared evidence, shared concepts and methods, and shared context. The resulting correlation is usually positive and reinforces shared errors.
    - Sec. 2.3: the Conditional Jury Theorem keeps both conclusions when votes are independent given the facts and every voter is competent given every value of the facts.
    - Sec. 2.4: conditional independence needs rich facts, and conditional competence needs coarse facts, so the two premises are almost never justified together.
    - Sec. 2.5 states the Competence-Sensitive Jury Theorem (Dietrich and Spiekermann 2013a). Assume votes are independent given the facts, and specific competence merely tends to exceed 1/2. Then majority reliability still increases with group size, but its limit is below 1 unless voters are competent under every value of the facts. The limit equals the probability that the facts are truth-conducive plus half the probability that they are neutral.
    - Sec. 3.2: when competence is heterogeneous, majority reliability can fall as members are added.
    - Sec. 3.3: with no diversity, judgments coincide and the correctness events are equivalent.
  - Headline numbers (verbatim, with location): none; the entry is conceptual.
  - Authors' own stated limitations or scope: the authors argue that the infallibility conclusion is untenable for real large bodies, and treat increasing reliability as the defensible version of the wisdom of crowds (Sec. 1.1). They call adequate modelling of voter dependence a central open challenge (Sec. 3.3, last paragraph).
  - Relation to the review: precedent and support for the review's majority-voting analysis at a key decision (RQ3; commitment C4). The Competence-Sensitive Jury Theorem is the formal counterpart of "independent votes help only when e_key < 1/2". Votes are independent given the facts of a decision, and where those facts mislead (competence below 1/2), adding voters drives the majority to the wrong answer.
  - The hinge: the voters are distinct individuals deciding a binary question with a fixed correct answer. In the review, the voters are samples from one or several LLMs at a key decision, and the shared prompt and model weights play the role of the common causes.
- Use 1 — intended claim: "Condorcet's jury theorem states that if each voter is independently right with the same probability above one half, the probability that the majority is right rises toward one as voters are added; the conclusion depends on independence, and correlated votes can stop it."
  - Source passage: "converges to a value which is below 1 unless CC holds" (Sec. 2.5, statement of the Competence-Sensitive Jury Theorem). The Condorcet statement is paraphrased above from Sec. 2.1, and positive correlation through common causes from Sec. 2.2.
  - Scope: the first half matches Sec. 2.1 exactly. The second half needs the mechanism. Correlation by itself does not stop convergence: the Conditional Jury Theorem (Sec. 2.3) still converges to 1 when votes are correlated through the state but every voter is competent given every state. The limit drops below 1 when the shared facts sometimes mislead, that is, when competence is 1/2 or less given those facts (Secs. 2.4–2.5).
  - Verdict: NARROW → safe wording: "Condorcet's jury theorem states that if voters are independently right, each with the same probability above one half, the probability that the majority is right increases with group size and converges to one. Shared evidence and other common causes usually make votes positively correlated. When votes are independent only given these shared facts, and the facts sometimes mislead the voters, majority reliability still increases with group size but converges to a limit below one: the probability that the shared facts point to the truth, plus half the probability that they are neutral [dietrich2023jury]."
- Bib notes: author, title, edition, editors, publisher, year and URL are taken from the SEP citation page. The SEP's own BibTeX string drops the second author (it reads `Dietrich, Franz and }`); fixed to Dietrich, Franz and Spiekermann, Kai. The entry type is `@incollection`, as the SEP recommends. The edition goes in the booktitle, "(Spring 2023 Edition)", so that IEEEtran does not print "ed." after it. Key year 2023 matches the edition. The current dynamic page and the Spring 2023 archive differ only in site navigation.

### ladha1992condorcet
- Source of record: https://doi.org/10.2307/2111584 (American Journal of Political Science 36(3):617–634, Aug. 1992). Access: not opened (JSTOR returned a "Client Challenge" bot check, which was not bypassed). Unpaywall and OpenAlex list no open copy, and the RePEc record of the 1991 working-paper version (Washington University in St. Louis, Political Economy paper 155) has no download. Metadata verified against Crossref, OpenAlex and the SEP bibliography.
- Retraction: the Crossref record has no update-to, updated-by or relation fields; OpenAlex has is_retracted = false.
- Card:
  - Setting: a theoretical generalization of Condorcet's jury theorem to correlated votes, applied to free speech and to a chief executive's choice of advisers. This comes from OpenAlex's abstract field, which reproduces the article's first page and is truncated.
  - What it establishes (metadata level only):
    - The first-page text, via OpenAlex, says the paper generalizes the theorem to correlated votes. It adds that for large groups Condorcet's result holds under fairly general conditions, while for small groups the conditions are severe. The text stops mid-sentence after that.
    - SEP Sec. 3.3 (Jury Theorems, Spring 2023) cites Ladha (1992) only as an example of modelling voter dependence through pairwise correlations. It does not state his conditions or results.
    - SEP Sec. 3.2 cites Ladha (1993), a different paper on interchangeable voters.
  - Headline numbers (verbatim, with location): none available.
  - Authors' own stated limitations or scope: not available (full text not opened).
  - Relation to the review: RQ3/C4. It is a precedent for majority voting with correlated voters.
  - The hinge: the paper models votes by people with pairwise correlations between voters; in the review the votes are samples from LLMs.
- Use 1 — intended claim: "Ladha showed that a majority can still outperform its members when votes are positively correlated, provided the average correlation is low enough."
  - Source passage: "I generalize CJT for correlated votes" (the article's first page as indexed in OpenAlex's abstract field; full text not opened). The SEP passage is paraphrased above with its location.
  - Scope: nothing beyond the first page could be checked. The condition on the average correlation is attributed to this paper by secondary sources, but it was not seen in the primary text, and the SEP does not state it.
  - Verdict: NARROW → safe wording: "Ladha extended Condorcet's jury theorem to correlated votes [ladha1992condorcet]." The clause "provided the average correlation is low enough" is DROPPED unless the authors open the article themselves (JSTOR access) and record the condition and its location.
- Bib notes: from Crossref: DOI, volume 36, issue 3, first page 617, Aug. 1992, single author Krishna K. Ladha. The last page, 634, comes from the SEP bibliography, because Crossref gives only the first page. The title is as in Crossref, with {Condorcet} protected.

### krogh1995neural
- Source of record: https://proceedings.neurips.cc/paper_files/paper/1994/hash/b8c37e33defde51cf91e1e03e51657da-Abstract.html (Advances in Neural Information Processing Systems 7, Proceedings of the 1994 Conference, G. Tesauro, D. S. Touretzky, T. K. Leen, eds.; MIT Press, 1995; pp. 231–238). Access: full text (proceedings PDF https://proceedings.neurips.cc/paper_files/paper/1994/file/b8c37e33defde51cf91e1e03e51657da-Paper.pdf, 8 pp.). It is a scan with an OCR layer; pp. 232–233 were read as page images to check the equations.
- Retraction: there is no Crossref record (NIPS 1994 papers have no DOIs, and the query returned unrelated items). The proceedings page shows no erratum, and there is no arXiv version.
- Card:
  - Setting: ensembles ("committees") of neural networks for regression under quadratic error. The ensemble output is a weighted average of member outputs, with positive weights that sum to one (Sec. 2, p. 232). Later sections cover cross-validation ensembles, optimal weights and active learning.
  - What it establishes:
    - The ambiguity decomposition (Sec. 2, eqs. 2–6, p. 232). At each input x, the ensemble's squared error equals the weighted average of the members' squared errors minus the ensemble ambiguity. The ambiguity is the weighted variance of the member outputs around the ensemble output.
    - Averaged over inputs, E = Ē − Ā (eq. 10, p. 233). Hence the ensemble error never exceeds the weighted average member error (eq. 11 for uniform weights, p. 233).
    - The ambiguity term carries all correlations between the networks and can be estimated from unlabeled data (p. 233).
    - Raising ambiguity without raising individual errors improves generalization (Sec. 3, p. 233).
  - Headline numbers (verbatim, with location): the identity E = Ē − Ā (eq. 10, p. 233). No empirical number is needed for this use.
  - Authors' own stated limitations or scope: the derivation is for approximating real-valued functions, i.e. regression (Sec. 1, p. 232). The authors stress that the constraint that weights sum to one is essential for the results (Sec. 2, p. 232).
  - Relation to the review: a precedent for C4/RQ3. An ensemble gains nothing on inputs where its members agree, and a set of identical members gains nothing at all.
  - The hinge: the paper averages real-valued outputs under squared error. The review aggregates discrete answers by majority vote, where this identity does not apply in this form.
- Use 1 — intended claim: "The error of an ensemble average equals the average error of its members minus their ambiguity, a measure of how much they disagree, so an ensemble gains only where its members differ."
  - Source passage: "is only useful if they disagree on some inputs" (Sec. 1, p. 232, about combining several predictors). The decomposition is eq. (6) per input and eq. (10) averaged, pp. 232–233.
  - Scope: regression, quadratic loss, convex weighted averaging of member outputs.
  - Verdict: NARROW → safe wording: "For regression under squared error, Krogh and Vedelsby showed that the error of a weighted ensemble average equals the weighted average error of its members minus the ensemble ambiguity, the spread of the members' outputs around the ensemble output; the ensemble therefore gains only on inputs where its members disagree [krogh1995neural]."
- Bib notes: authors and title come from the proceedings page and PDF. The NeurIPS site's .bib gives year 1994 (the conference year), editors, MIT Press, and empty pages. The printed volume appeared in 1995: MIT Press, Cambridge, MA, publish date July 6, 1995, per the Open Library record for ISBN 9780262201049, since the MIT Press page returned 403. Pages 231–238 come from the running heads in the proceedings PDF (232, 233, 235 and 237 are printed; the paper has 8 pages). The .bib uses year 1995 to match the printed volume and the assigned key. If the authors prefer the NeurIPS site convention, change the year to 1994.

### kuncheva2003measures
- Source of record: https://doi.org/10.1023/A:1022859003006 (Machine Learning 51(2):181–207, May 2003, Kluwer). Access: full text (the Springer page offers "Download PDF" free of charge; https://link.springer.com/content/pdf/10.1023/A:1022859003006.pdf, all 27 pages read).
- Retraction: the Crossref record has no relation fields, and there is no arXiv version.
- Card:
  - Setting: ten diversity statistics computed on the "oracle" outputs (correct or incorrect) of classifier teams (Secs. 3–4, Table 2). Four are pairwise: the Q statistic, correlation, disagreement and double fault. Six are non-pairwise: entropy, difficulty, Kohavi–Wolpert variance, interrater agreement, generalized diversity and coincident failure diversity. The four experiments are summarized in Table 3 (Sec. 6):
    - Simulated teams with L in {3, 5, 9}, individual accuracy p in {0.6, 0.7}, N = 1000 objects and controlled average pairwise Q (315 teams).
    - An enumeration of all 563 teams with L = 3, p = 0.6 and N = 30.
    - 14,700 teams of three linear or quadratic classifiers built on feature subsets of the Wisconsin breast cancer data.
    - Bagging and random weak classifiers (L = 9) on the Phoneme and Cone-torus data, over 500 train/test splits.
  - What it establishes:
    - Sec. 6.2, Fig. 2, p. 193 (members of equal accuracy with equal pairwise dependence, simulated). Every measure tracked the majority-vote gain closely. Lower Q (more diverse) gave larger gains, and negative dependence beat independence. The worst case was positively dependent but non-identical members, and those teams sometimes fell below the single best member.
    - Sec. 6.3, pp. 194–195 (unequal pairwise dependencies, enumeration). The relationship weakened, and a negatively correlated team could still vote below the individual accuracy. For every measure there was still a threshold beyond which improvement over the individual was guaranteed.
    - Secs. 6.4–6.5, Tables 7 and 9, pp. 196–200 (real data). The diversity measures were only weakly related to the gain from combining. The authors judged them to have no useful predictive value in the breast cancer experiment.
  - Headline numbers (verbatim, with location):
    - Table 5 (p. 193): the extreme rank correlations between the measures and the majority-vote gain lie between 0.9371 and 0.9949 in absolute value.
    - Sec. 6.3 (p. 195): the rank correlations with P_maj were −0.5127 for Q_av and 0.7379 for coincident failure diversity; the other eight measures all had absolute value 0.5210.
    - Table 7 (p. 197), majority-vote row: the largest absolute correlation with P_team − P_max is 38% (coincident failure diversity).
  - Authors' own stated limitations or scope:
    - The conclusions rest on a particular set of experiments. Diversity and accuracy might relate more strongly in other settings, such as AdaBoost (Sec. 7, p. 203).
    - In the breast cancer experiment, the improvements were small and only three classifiers were used (Sec. 6.4, p. 198).
    - The simulated distribution of Q was artificial (Sec. 6.2, pp. 193–194).
    - The authors still conclude that the motivation for building diverse classifiers is sound, but that measuring diversity usefully remains unsolved (Sec. 7, p. 204).
  - Relation to the review: C4/RQ3. It qualifies the role of diversity: positive dependence without identity is the worst case for majority voting, and measured diversity is a weak guide to the gain.
  - The hinge: the members are classical classifiers with set accuracies on classical data sets, in small teams (3 to 9), with binary correct/incorrect outputs. In the review, the voters are LLM samples whose dependence is not set by design.
- Use 1 — intended claim: "diversity among classifiers is what lets majority voting improve on its members, although the link between measured diversity and ensemble accuracy proved weaker in practice than in theory."
  - Source passage: "our results raise some doubts about the usefulness of diversity measures" (Abstract, p. 181). The same sentence of the abstract notes proven links between diversity and accuracy in some special cases. The rest is paraphrased above with locations.
  - Scope: the paper does not establish that diversity is the cause of voting gains. It reports the field's motivation (Sec. 1) and an example of a highly diverse team that voted worse than its members (Sec. 6.3). "Weaker in practice" is supported for its real-data experiments.
  - Verdict: NARROW → safe wording: "Kuncheva and Whitaker compared ten measures of diversity among classifiers with the gain of majority voting over the team's members. In simulations with equal member accuracies and equal pairwise dependence, more diverse teams gained more, and positively dependent but non-identical members did worst. On real data sets the measures predicted the gain poorly, and the authors doubted their usefulness for building ensembles, while keeping diversity as a sound motivation [kuncheva2003measures]."
- Bib notes: checked against Crossref (DOI, volume 51, issue 2, pages 181–207, May 2003) and the PDF header (Machine Learning, 51, 181–207, 2003, Kluwer). Full author names come from the PDF byline, and the month from the Springer page ("Published: May 2003").

### eckhardt1985theoretical
- Source of record: https://doi.org/10.1109/TSE.1985.231895 (IEEE Transactions on Software Engineering SE-11(12):1511–1517, Dec. 1985). Access: full text of the precursor report, NASA Technical Memorandum 86369 (January 1985), titled "A Theoretical Basis for the Analysis of Redundant Software Subject to Coincident Errors". It is NTRS 19850015006, https://ntrs.nasa.gov/api/citations/19850015006/downloads/19850015006.pdf, 41 pp., read in full. The TSE article itself was not opened (IEEE Xplore returned an empty bot-protection response, not bypassed). Its abstract, from the NTRS reprint record 19870030726, matches the TM's framework. Every location below refers to the TM.
- Retraction: the Crossref record has no relation fields, and there is no arXiv version.
- Card:
  - Setting: a probability model of N-version software with a perfect majority voter (TM Sec. 2).
    - Versions are a random sample from a real or conceptual population of programmers who develop independently to a common specification.
    - Inputs arrive as a stationary, independent series drawn from a usage distribution.
    - The intensity of coincident errors θ(x) is the proportion of the population whose version fails on input x.
  - What it establishes:
    - Theorem 2 (TM Sec. 3): the failures of the versions are unconditionally independent if and only if θ(x) is constant over the inputs, except on a set of probability zero. For two versions, eqs. 13–15 show that the joint failure probability minus the product of the individual ones equals the variance of θ across inputs. So any variation in θ makes joint failure more likely than independence predicts. A coin example gives 0.26 against 0.25 (TM Sec. 3).
    - A low average intensity does not imply independence; the variance of the intensity distribution measures the departure from independence (TM Secs. 3, 6). Particular pairs of versions can even be negatively dependent. The theorem concerns the average over repeated selections of versions (TM Sec. 3).
    - Theorem 3 (TM Sec. 4): N versions beat one version if the intensity distribution meets an asymmetry condition about 1/2, for instance if θ(x) ≤ 1/2 almost everywhere. An average version failure probability below 1/2 does not by itself guarantee a gain (end of TM Sec. 4).
    - TM Sec. 5:
      - As N grows, the failure probability tends to the probability mass of inputs on which more than half of the population fails, plus half the mass at exactly one half (eq. 23).
      - An intermediate N can be optimal (Fig. 4, N = 7).
      - If θ(x) > 1/2 on a set of positive probability, adding versions can make the system worse than a single version (Figs. 5a–b).
  - Headline numbers (verbatim, with location): these are illustrative and use the hypothesized intensity distribution of Table 1a (TM Sec. 5, Fig. 1).
    - The average version failure probability is 2 × 10⁻⁴.
    - With N = 5, the failure probability falls by about two orders of magnitude, whereas the independence model predicts more than five.
    - Reaching a failure probability below 10⁻⁹ needs 17 versions, not the 5 that independence predicts.
  - Authors' own stated limitations or scope (TM Sec. 6):
    - The intensity distributions are hypothesized, some with deliberately high intensity, and empirical data are needed.
    - Developing a version is equated with drawing a program at random from a population of independently developed programs.
  - Relation to the review: a precedent for RQ2/RQ3 and C4. Heterogeneous difficulty across inputs creates dependence between independently produced solvers. The limit of majority voting is set by the share of inputs on which most solvers fail, and the best N can be finite. This is the same structure as the review's majority-vote analysis at key decisions and as Chen et al. (2024), forty years earlier.
  - The hinge: the voters are programs drawn from a population of human developers and run on a random stream of inputs. In the review, the voters are LLM samples and the "inputs" are key decisions within an answer.
- Use 1 — intended claim: "Even versions of a program developed independently fail together more often than independence predicts, because inputs differ in how hard they are."
  - Source passage: "a constant intensity characterizes the case of independence" (TM Sec. 6, Conclusions). Theorem 2 and eqs. 13–15 are paraphrased above.
  - Scope: this is a result of a theoretical model, not an observation. It concerns averages over random selection of versions, and the excess joint failure for a pair equals the variance of θ. The authors expect that a constant intensity seldom holds (TM Secs. 3, 6).
  - Verdict: NARROW → safe wording: "Eckhardt and Lee modelled independently developed program versions as random draws from a population of developers. Even then, the versions fail independently only if every input is equally likely to defeat a randomly drawn version; when this failure intensity varies across inputs, as the authors expect it usually does, versions fail together more often than independence predicts [eckhardt1985theoretical]."
- Bib notes:
  - TSE metadata (title, volume SE-11, issue 12, pages 1511–1517, Dec. 1985, DOI) come from Crossref.
  - Author full names and "Jr." come from the TM title page ("Dave E. Eckhardt, Jr. and Larry D. Lee") and the NTRS record of the TSE reprint ("Eckhardt, D. E., Jr.").
  - The TSE title says "Multiversion Software" where the TM says "Redundant Software".
  - Because the TSE text was not opened, the TSE theorem numbering is unverified. In the appendix, cite TSE without theorem numbers, or also cite the TM.
  - Optional TM entry, not in J3_voting.bib: techreport; Eckhardt, Jr., Dave E. and Lee, Larry D.; title as above; NASA Technical Memorandum 86369; NASA Langley Research Center, Hampton, VA; Jan. 1985; https://ntrs.nasa.gov/citations/19850015006.

### knight1986experimental
- Source of record: https://doi.org/10.1109/TSE.1986.6312924 (IEEE Transactions on Software Engineering SE-12(1):96–109, Jan. 1986). Access: full text of the authors' manuscript hosted on Nancy Leveson's MIT site, http://sunnyday.mit.edu/papers/nver-tse.pdf. The host timed out, so the Internet Archive capture of 5 Jan 2026 was read: http://web.archive.org/web/20260105044654/http://sunnyday.mit.edu/papers/nver-tse.pdf (all sections and tables). The IEEE version was not opened (IEEE Xplore bot protection, not bypassed). Page numbers in the manuscript differ from the journal's, so locations are given as sections and tables.
- Retraction: the Crossref record has no relation fields, and there is no arXiv version. This is not a retraction, but the experiment was publicly disputed by N-version programming proponents (Avizienis and former students). The authors answered in "A Reply to the Criticisms of the Knight & Leveson Experiment" (author copy at sunnyday.mit.edu/critics.pdf, Internet Archive capture; only its introduction was read).
- Card:
  - Setting: 27 versions of the "launch interceptor" program, an anti-missile radar decision problem with 241 Boolean results per test case (Secs. 2–4).
    - The programmers were graduate and senior students at the University of Virginia (9) and UC Irvine (18). They worked independently in Pascal from one specification.
    - Each version passed a 200-case acceptance test.
    - Each was then run on 1,000,000 randomly generated test cases, and its results were compared with a "gold" version.
  - What it establishes:
    - The versions were individually very reliable. Six recorded no failures, and 23 of the 27 succeeded on more than 99.9% of tests (Sec. 4, Table 1).
    - Coincident failures: on 1,255 of the million test cases two or more versions failed, and on two of them eight versions failed (Sec. 4, Table 2). The coincident failures involved versions from both universities (Table 3).
    - Under the independence model, the number of tests with more than one failure is binomial. The normal approximation gives z = 100.51 against a 99% critical value of 2.33, so the independence assumption was rejected (Sec. 5).
    - About half of the faults found involved two or more programs. The authors hypothesize that some parts of a problem are inherently harder than others (Sec. 8).
  - Headline numbers (verbatim, with location):
    - Sec. 5: N = 27 versions, n = 1,000,000 tests, K = 1255, z = 100.51.
    - Table 2: 551, 343, 242, 73, 32, 12 and 2 tests on which exactly 2, 3, 4, 5, 6, 7 and 8 versions failed.
    - The expected count under independence is not printed. Our arithmetic from the Table 1 failure counts gives about 127 (z ≈ 100.2), consistent with the paper.
  - Authors' own stated limitations or scope:
    - The conclusion holds for the particular problem programmed and may not extend to other programs (Sec. 8).
    - The programs were small, 327 to 1,004 lines (Sec. 7).
    - Sec. 7 defends the use of student programmers and of random tests.
  - Relation to the review: an empirical precedent for RQ3/C4. Independently produced solvers share failures far beyond independence, and the authors' difficulty hypothesis links this to RQ2.
  - The hinge: the solvers are human-written programs for one specification, tested on randomly generated inputs. In the review, the voters are samples from LLMs at key decisions.
- Use 1 — intended claim: "In an experiment with 27 independently written versions of one program, coincident failures occurred far more often than independence predicts, and the independence hypothesis was rejected."
  - Source passage: "we reject the null hypothesis with a confidence level of 99%" (Sec. 5). The numbers are given above. The abstract calls the number of tests with more than one failure substantially more than expected.
  - Scope: one application (the launch interceptor problem), student programmers, Pascal, random inputs. The numbers are from the authors' manuscript.
  - Verdict: ACCURATE (for the one program studied). Optional fuller wording: "Knight and Leveson had 27 versions of one program written independently from the same specification and ran each on a million random inputs; 1,255 inputs defeated two or more versions, far more than an independence model predicts, and they rejected independence at the 99% level for that program [knight1986experimental]." Do not quote z to two decimals in the paper. The journal version could not be checked, and a third-party course summary of the paper gives 100.55. "z ≈ 100" is safe.
- Bib notes: Crossref supplied the title, volume SE-12, issue 1, pages 96–109, Jan. 1986, the DOI and the authors (John C. Knight, Nancy G. Leveson). Full names also match the manuscript byline. The manuscript title prints "Multi-Version"; Crossref and IEEE give "Multiversion", which is used.

### vaupel1979impact
- Source of record: https://doi.org/10.2307/2061224 (Demography 16(3):439–454, Aug. 1979). Access: full text. The scanned publisher PDF on James W. Vaupel's MPIDR publication page, https://user.demogr.mpg.de/jwv/pdf/Vaupel-Demography-16-1979-3.pdf (16 pp., journal pages 439–454), was read as page images. Duke University Press showed a Cloudflare challenge, and SpringerLink offers only subscription access; neither was bypassed.
- Retraction: the Crossref record has no relation fields. PubMed ID is 510638. There is no arXiv version.
- Card:
  - Setting: demographic life-table theory with heterogeneous frailty.
    - Frailty z multiplies a standard age-specific force of mortality: μ(x, z) = z·μ(x, 1) (eqs. 1a–1c, pp. 440–441). It is fixed for life.
    - Frailty at birth is gamma distributed, with shape k = 1, 4 or 8 (eq. 7, p. 442).
    - The illustrations use Swedish females born in 1875, and Swedish females and males in 1975.
  - What it establishes:
    - The cohort's force of mortality equals the standard individual's force times the mean frailty of the survivors (eq. 6b, p. 441). Because frail individuals tend to die first, mean frailty falls with age, so individual mortality rises faster than cohort mortality (p. 441). With gamma frailty and k = 1, mean frailty is 1/(1 + H(x)) (eq. 9c, p. 442).
    - Fig. 3 (p. 446) and p. 443: the cohort curve cuts through the individual curves at ever lower frailty, and cohort rates rise less rapidly than any individual's.
    - Life tables that ignore heterogeneity overestimate life expectancy and the gains from interventions. They underestimate individual aging, past progress against mortality, and mortality differentials (Abstract, p. 439; Discussion, p. 451).
  - Headline numbers (verbatim, with location):
    - p. 447, with k = 1: the force of mortality of individuals aged 84 was 8.1 times greater in 1875 than in 1975, but only 60 percent greater for the cohort.
    - Table 2 (p. 450): Swedish female life expectancy at birth for 1975 is 78.15 as currently calculated and 76.36 adjusted with k = 1.
  - Authors' own stated limitations or scope:
    - Constant frailty is a first approach. A fuller model would let frailty vary, have many components and be cause-specific (p. 440).
    - Frailty is hard to define and measure (Discussion, p. 451).
    - The Swedish calculations are illustrative (pp. 443, 451).
  - Relation to the review: a precedent for the review's argument that pooled curves need not follow one exponential (RQ1/RQ2 heterogeneity). When units differ in risk, selection removes the high-risk units first, so the observed aggregate rate rises more slowly than every unit's own rate. The paper works with proportional hazards for human mortality; it does not discuss accuracy-versus-length curves or mixtures of constant hazards.
  - The hinge: this is human mortality, with frailty fixed for life and one common age schedule. The review's units are prompts or answers, with error hazards that act across positions or decisions.
- Use 1 — intended claim: "In a population whose members differ in frailty, the observed death rate rises more slowly with age than any individual's, because the frailest die first."
  - Source passage: "Cohort mortality rates thus increase less rapidly than mortality rates for any individual" (p. 443). On p. 441 the frail tend to die first; this is a tendency, not a rule.
  - Scope: the proportional frailty model, in which each individual's force of mortality is a fixed multiple of a common schedule. "Rises more slowly" compares the cohort's force of mortality with each individual's under that model.
  - Verdict: NARROW → safe wording: "Vaupel, Manton and Stallard modelled each person's death rate as a fixed multiple, the frailty, of a common age schedule. Because frailer people tend to die first, the average frailty of survivors falls with age, and the death rate observed for the cohort rises more slowly with age than the death rate of any individual in it [vaupel1979impact]."
- Bib notes: checked against Crossref (DOI, volume 16, issue 3, pages 439–454, Aug. 1979, publisher Duke University Press) and the scanned first page (Demography, Volume 16, Number 3, August 1979; authors James W. Vaupel, Kenneth G. Manton, Eric Stallard). The title is given in title case. Crossref has it in sentence case.

### chen2024more
- Source of record: https://proceedings.neurips.cc/paper_files/paper/2024/hash/51173cf34c5faac9796a47dc2fdd3a71-Abstract-Conference.html (NeurIPS 2024, Advances in Neural Information Processing Systems 37, pp. 45767–45790, DOI 10.52202/079017-1455). The OpenReview search API lists forum m5106RRLgx as "NeurIPS 2024 poster". Access: full text (proceedings PDF https://proceedings.neurips.cc/paper_files/paper/2024/file/51173cf34c5faac9796a47dc2fdd3a71-Paper-Conference.pdf, main text and Appendices A–D; Theorem 2 checked on the rendered p. 6). The arXiv abs page for 2403.02419 was also checked.
- Retraction: the Crossref record 10.52202/079017-1455 has no relation fields. arXiv 2403.02419 (v1 4 Mar 2024, v2 4 Jun 2024) is not withdrawn.
- Card:
  - Setting:
    - Two compound systems (Sec. 3): Vote, a majority vote over K i.i.d. LM answers, and Filter-Vote, which applies an LM filter before the vote.
    - Real tasks, posed as multiple choice (App. D.1): MMLU Physics (151 questions), TruthfulQA (817), GPQA diamond (198) and AVERITEC dev (500).
    - Generation (App. D.3): GPT-3.5-turbo-0125 at temperature 0.1, with 400 answers per question. Accuracy at K calls is estimated by resampling K of the 400 answers with replacement, averaged over 1,000 runs.
    - Synthetic datasets with two difficulty levels (Sec. 5).
  - What it establishes:
    - Accuracy can be non-monotone in the number of calls. Vote and Filter-Vote accuracy can first rise and then fall as calls are added (Fig. 1). In the AVERITEC case study, K runs from 2 to 1,000 (Fig. 4a).
    - Definitions (Def. 1 and Lemma 1, pp. 4–5): a query is easy if infinitely many calls give the correct answer and hard otherwise. For Vote, a query is hard when some wrong answer is more likely on a single call than the correct one.
    - More calls raise accuracy on easy queries and lower it on hard ones (Sec. 4.1, p. 6). On MMLU Physics, 53% of queries were easy and 47% hard for Vote (Fig. 2).
    - Theorem 2 (p. 6) uses two answer options and odd K. A fraction α of queries has single-call accuracy p1 > 1/2, and the rest has p2 < 1/2. The accuracy curve then rises, falls, rises then falls, or falls then rises, depending on whether p1 + p2 exceeds 1 and on how α compares with a threshold set by p1 and p2. Theorem 4 gives the optimal K.
    - A fitted scaling model predicts the empirical curves and the optimal K (Figs. 4c and 5; App. Table 2).
  - Headline numbers (verbatim, with location):
    - Fig. 4d (p. 8), AVERITEC examples: for an easy query, a single call gives the correct answer with probability 67%. For a hard query, it gives the correct answer with 34% and a wrong answer with 56%, so Vote converges to the wrong answer.
    - Fig. 6, synthetic data: difficulty (0.85, 0.4) gives a rise then a fall.
  - Authors' own stated limitations or scope:
    - Only two compound-system designs are studied (App. B, p. 19).
    - The tasks are relatively objective (App. B).
    - Predicting query difficulty without querying the LM remains open (App. B).
    - The cost of calls is not analysed (App. B).
    - The work focuses on tasks with a small number of possible answers (Sec. 1, p. 2).
  - Relation to the review: direct support for the review's majority-vote analysis at a key decision (RQ2/RQ3, C4). Voting helps where the correct answer is the single-call plurality (e_key < 1/2 in the binary case) and hurts where it is not. A mixture of the two gives non-monotone accuracy.
  - The hinge: the votes are resampled i.i.d. answers of one model to a whole question at low temperature. The review applies the same logic to key decisions inside long answers, where the decision points are not observed directly.
  - Note for the authors: the AVERITEC paragraph in Sec. 5 (p. 8) states the easy and hard directions reversed relative to the abstract, Sec. 4.1, Theorem 2 and the Fig. 4 caption. This looks like a typo in the paper. Cite Sec. 4.1, Theorem 2 or Fig. 4.
- Use 1 — intended claim: "The accuracy of voting over LLM calls can first rise and then fall as calls are added, because queries differ in difficulty: more calls help on easy queries and hurt on hard ones."
  - Source passage: "higher performance on easy queries, but lower performance on difficult queries" (Sec. 4.1, p. 6). The abstract presents the difficulty explanation as what the authors' theoretical results suggest.
  - Scope: one model (GPT-3.5-turbo-0125, temperature 0.1), four multiple-choice datasets and synthetic data. The theorem holds for a binary-answer model with two difficulty levels.
  - Verdict: NARROW → safe wording: "Chen et al. found that the accuracy of majority voting over repeated GPT-3.5 calls on multiple-choice benchmarks can first rise and then fall as calls are added. Their analysis attributes this to differences in query difficulty: more calls raise accuracy on queries where the correct answer is the most likely single-call output and lower it on queries where some wrong answer is more likely, so a task that mixes both kinds can show a peak [chen2024more]."
- Bib notes:
  - The proceedings metadata, the NeurIPS .bib, Crossref and OpenReview all give the title "Are More LLM Calls All You Need? Towards the Scaling Properties of Compound AI Systems", which is used. The camera-ready PDF's own title line reads "Are More LM Calls All You Need?". The arXiv and assignment title is the preprint's ("Towards Scaling Laws of Compound Inference Systems").
  - Authors follow the proceedings page and the PDF byline ("Jared Davis"). OpenReview and arXiv list "Jared Quincy Davis".
  - Pages and DOI come from the proceedings metadata.

### brown2024monkeys
- Source of record: https://arxiv.org/abs/2407.21787 (arXiv preprint; v3 of 30 Dec 2024, v1 of 31 Jul 2024). No published version was found:
  - The OpenReview search API lists note 0xUEBQV54B as "Submitted to ICLR 2025", with venueid ICLR.cc/2025/Conference/Rejected_Submission.
  - The authors' lab page (scalingintelligence.stanford.edu) lists the work as "Preprint, 2024".
  - A web-search summary claiming "ICLR 2025" was wrong.

  Access: full text (arXiv PDF v3, all sections including Apps. A and D).
- Retraction: arXiv shows three versions and no withdrawal. There is no Crossref record; the arXiv DOI is registered with DataCite, and the Crossref query returned unrelated items.
- Card:
  - Setting: repeated independent sampling from one model per problem, at positive temperature.
    - Tasks (Sec. 2): GSM8K (128 test problems), MATH (128), MiniF2F-MATH (Lean4), CodeContests and SWE-bench Lite.
    - Models: Llama-3-8B/70B-Instruct, with 10,000 samples per problem and temperature 0.6 for GSM8K and MATH (Apps. A.3–A.4). Gemma and Pythia families were also used. SWE-bench Lite used DeepSeek-Coder-V2-Instruct with 250 attempts per issue.
    - Coverage is pass@k with the unbiased estimator. For GSM8K and MATH, an oracle checks the final answer.
  - What it establishes:
    - Coverage rises with the number of samples across tasks and models (Figs. 2–3). On SWE-bench Lite it rises from 15.9% with one sample to 56% with 250. On CodeContests, Gemma-2B rises from 0.02% to 7.1% at 10,000 samples (Secs. 1, 2.1).
    - log(coverage) often follows an approximate power law in k, so coverage ≈ exp(a·k^b). For Llama-3 and Gemma models, coverage grows nearly log-linearly over several orders of magnitude (Sec. 1; Sec. 3.1, Fig. 5). Some curves do not fit closely; Llama-3-8B-Instruct on MiniF2F-MATH is the most striking case (Fig. 5 caption; Sec. 3.1).
    - On GSM8K and MATH, three selection methods plateau at around 100 samples while coverage keeps rising past 95% (Sec. 4.1, Fig. 7). The methods are majority vote, reward-model best-of-N and reward-weighted vote (ArmoRM-Llama3-8B-v0.1). The authors note that rare correct samples cannot change the most common answer.
  - Headline numbers (verbatim, with location): Sec. 1, Llama-3-8B-Instruct on MATH. Coverage is 82.9% at 100 samples and 98.44% at 10,000. Over the same range, majority voting and reward models improve at most from 40.50% to 41.41%.
  - Authors' own stated limitations or scope:
    - Sampling is simple: attempts are independent and use the same prompt and hyperparameters. Temperature is the only source of diversity, and there is a single turn (Sec. 5).
    - Verification without automatic tools is left open (Sec. 5).
    - The paper is inconsistent about where selection plateaus: beyond several hundred samples in the abstract, about 100 in Sec. 1 and Sec. 4.1, and before 100 in the Fig. 7 caption.
  - Relation to the review: RQ3/C4. It supports the review's distinction between a correct answer existing among the samples and the majority being correct. On hard problems, rare correct samples raise coverage but cannot win a plurality. It qualifies the view that more samples help: they help selection only where the correct answer is common.
  - The hinge: coverage is measured with an oracle or automatic verifier at the level of whole answers. The review's analysis concerns error rates at individual decisions within answers.
- Use 1 — intended claim: "Coverage, the fraction of problems solved by at least one sample, grew roughly log-linearly with the number of samples over several orders of magnitude, while majority voting and reward-model selection plateaued."
  - Source passage: "coverage increases from 82.9% with 100 samples to 98.44% with 10,000 samples" (Sec. 1, Introduction; Llama-3-8B-Instruct on MATH).
  - Scope:
    - The near log-linear growth is "often", stated for Llama-3 and Gemma models over the sampled range (at most 10,000 samples). Coverage is bounded by 1, and the fitted form is an exponentiated power law.
    - The plateau is shown only for GSM8K and MATH, the tasks without automatic verifiers, with Llama-3-8B/70B-Instruct.
  - Verdict: NARROW → safe wording: "Brown et al. found that coverage, the fraction of problems solved by at least one sample, kept rising as samples were added, up to 10,000 per problem, on math and coding tasks, often close to log-linearly in the number of samples. On GSM8K and MATH, majority voting and reward-model selection stopped improving after about a hundred samples: for Llama-3-8B-Instruct on MATH, coverage rose from 82.9% at 100 samples to 98.44% at 10,000, while the best selection method rose only from 40.50% to 41.41% [brown2024monkeys]."
- Bib notes: authors and title are from the arXiv abs page (Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Ré, Azalia Mirhoseini). It is arXiv-only, so the entry is `@misc` with howpublished, DOI 10.48550/arXiv.2407.21787 and note Preprint. The version read is v3. Do not cite ICLR.

### toups2023ecosystem
- Source of record: https://proceedings.neurips.cc/paper_files/paper/2023/hash/a0b1082fc7823c4c68abcab4fa850e9c-Abstract-Conference.html (NeurIPS 2023, Advances in Neural Information Processing Systems 36, pp. 51178–51201, DOI 10.52202/075280-2228). Access: full text (proceedings PDF https://proceedings.neurips.cc/paper_files/paper/2023/file/a0b1082fc7823c4c68abcab4fa850e9c-Paper-Conference.pdf, main text; Table 1 checked on the rendered p. 4). The arXiv abs page for 2307.05862 carries the comment "Published at NeurIPS 2023".
- Retraction: the Crossref record has no relation fields. arXiv (v1 12 Jul 2023, v2 3 Apr 2024) shows no withdrawal.
- Card:
  - Setting: the HAPI audit (Chen et al. 2022a) of commercial ML APIs, plus a dermatology study (DDI).
    - HAPI uses three commercial APIs per task, from Google, Microsoft, Amazon, IBM, Baidu and Face++. The three tasks cover three modalities: sentiment analysis, facial emotion recognition and spoken command recognition.
    - It spans eleven datasets, with predictions from 2020 to 2022 (Sec. 3.1).
    - DDI has 656 skin-lesion images, classified by two models and two board-certified dermatologists (Sec. 5).
  - What it establishes:
    - Systemic failure means an instance misclassified by every system (Sec. 2.1).
    - The baseline assumes independent failures at each model's observed error rate (a Poisson-Binomial distribution). Against it, instances failed by all systems and instances got right by all are both more frequent than baseline in every HAPI dataset. Intermediate outcomes are mostly less frequent (Finding 1, Sec. 3.2, Fig. 2).
    - When one model improves, the improvement seldom reaches systemic failures. On average, 10% of a model's improvement falls on instances that all other models fail, although such instances make up 27% of its possible improvements (Sec. 1; Finding 2, Sec. 4).
    - Sec. 6.1: example difficulty partly explains the homogeneity. The evidence comes from annotator disagreement on FER+ and dermatologist errors on DDI. A two-level easy/hard model fits only if about 25% of instances are about 3.5 times harder. Model-centric explanations (shared data or architectures, "algorithmic monoculture") could not be tested.
  - Headline numbers (verbatim, with location):
    - Table 1 (p. 4), DIGIT: model error rates 0.217, 0.259 and 0.472; systemic failure rate 0.129. Our arithmetic: independence would give 0.217 × 0.259 × 0.472 ≈ 0.027.
    - Sec. 3.1: the systemic failure rate is often about half the error rate of the most accurate model.
  - Authors' own stated limitations or scope:
    - Independence is chosen as a neutral baseline. The authors decline to correct for "hardness" because hardness is observer-relative (Sec. 3.2). A correlated baseline is explored in App. A.3.
    - They cannot test model-centric explanations because little is known about the commercial systems (Sec. 6.1).
  - Relation to the review: support for RQ3/C4. It shows error dependence across separately developed deployed models. The authors' own partial explanation, shared example difficulty, connects to RQ2.
  - The hinge: the systems are commercial classifiers on fixed-label datasets with 2 to 31 classes, observed in 2020–2022. The review concerns LLMs on generation and reasoning, with errors judged on whole answers.
- Use 1 — intended claim: "Across deployed commercial machine-learning systems, the same instances are failed by every system more often than independent failures would predict (systemic failure)."
  - Source passage: "the observed rate always exceeds the baseline rate for the homogeneous outcomes" (Sec. 3.2, Finding 1). DDI models and dermatologists show the same pattern (Finding 3, Sec. 5.2).
  - Scope: the eleven HAPI datasets, each with three commercial systems, plus DDI. "Systemic failure" names the event of being failed by every system, not the excess over baseline.
  - Verdict: NARROW → safe wording: "In an audit of commercial machine-learning APIs, with three systems per task across sentiment analysis, facial emotion recognition and spoken command recognition on eleven datasets, instances misclassified by every system (systemic failures) were more frequent than independent failures would predict on every dataset, as were instances that every system classified correctly [toups2023ecosystem]."
- Bib notes:
  - Author names follow the authors' own byline in the proceedings PDF, which arXiv matches: Kathleen A. Creel, Sarah H. Bana, Percy Liang.
  - The NeurIPS .bib and proceedings metadata shorten these to "Creel, Kathleen" and "Bana, Sarah", and give "Liang, Percy S."
  - Pages 51178–51201 and the DOI come from the proceedings metadata.
  - The title matches the proceedings, Crossref and arXiv.
  - The entry passes a test run of bibtex with IEEEtran.bst.
