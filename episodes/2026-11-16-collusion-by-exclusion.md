---
title: Collusion by exclusion: how a bid-rigging cartel can exploit preselection (Seibel & Škoda, AEJ Micro 2026)
date: 2026-11-16
status: ready
paper: Seibel, R. and Škoda, S. (2026). Collusion by Exclusion in Public Procurement. American Economic Journal: Microeconomics 18(3), 148-202. DOI 10.1257/mic.20240308.
link: https://doi.org/10.1257/mic.20240308
sources_read: the author-hosted PDF dated August 2025 on Samuel Škoda's website, essentially the full text (main text, conclusion, most appendix discussion), read via automated extraction in two passes; the published AEJ Micro version was not read
summary: A theory of how a partial bid-rigging cartel can use bidder preselection to shut out competitive rivals, a collusion marker built from near-identical opening bids, and what happened in Slovak public procurement when the preselection stage was removed in 2017.
caveats: All figures come from the August 2025 author version and may differ from the published article. The extraction showed small inconsistencies between the text and tables, for example the reform effect on cartel members facing each other, so those numbers are given as ranges. The convicted-cartel validation rests on one case of six firms and 274 auctions in the data. The 2017 reform bundled preselection removal with other rule changes. The euro counterfactuals are illustrative. Not covered: the published version's revisions, the extension appendices in detail.
---
# Script for a ~20 minute episode. Numbers only from the Seibel and Skoda working paper, August 2025 version. Style in [brackets]; <short pause> and |backchannels| are Gemini TTS markup.

MAYA [curious, conversational]: Here's a design choice that sounds like pure good governance. A government agency buying goods runs an auction, but first it screens the field. Everyone submits a sealed opening bid, and only the best three move on to the real auction.
THEO: Sensible. You don't want a hundred bidders clogging the main event.
MAYA: And in theory, when everyone is competing honestly, it doesn't cost you anything. <short pause> The question in today's paper is what happens when some of those bidders are in a cartel.
THEO: Ah. Because a cartel that knows the rule is "top three advance" has a very simple plan.
MAYA: Fill all three slots with your own people.
THEO: Which shuts out everyone else before the real competition even starts.
MAYA: Exactly. The paper is Collusion by Exclusion in Public Procurement, by Regina Seibel and Samuel Škoda, in the American Economic Journal: Microeconomics this year. I'm working from the author's August twenty twenty-five version, not the published one.
THEO: And it's theory plus data, I take it.
MAYA: Three pieces. A model of how a partial cartel exploits preselection. A marker for spotting cartel members from opening bids alone. And a natural experiment, where Slovakia removed the preselection stage in twenty seventeen.
THEO: So we get a prediction, a detection tool, and a policy change to test them against.
MAYA: That's the structure. Let's start with the institution, because it matters a lot.
THEO: Go.
MAYA: The setting is Slovakia's electronic contracting system, which the paper abbreviates E K S. It's mandatory for standardized goods and services with contract values between five thousand and a hundred thirty-five thousand euros.
THEO: So not giant infrastructure projects. Everyday purchases.
MAYA: Everyday purchases, and crucially, the procuring agency cannot choose the auction format. The system dictates it.
THEO: Which removes a classic worry, that agencies pick formats because they suspect collusion.
MAYA: Right. Now the format. Before the reform, a bidder first had a window of at least seventy-two hours to submit a sealed opening bid.
THEO: |Mm-hm.|
MAYA: The three lowest opening bids advanced to the main auction. That was a reverse English auction, starting at the lowest opening bid, running at least twenty minutes, with a two-minute extension whenever a new bid came in. And bidder identities were hidden.
THEO: So the opening bid does two jobs. It's a ticket to the main stage, and it sets the starting price.
MAYA: Exactly. Then on the first of February twenty seventeen, the rule changed. Everyone who submitted an opening bid could enter the main auction. No more cut.
THEO: Was that announced ahead of time?
MAYA: The authors describe the reform as coming without advance notice, which helps if you worry about firms adjusting beforehand.
THEO: Okay. Hold that thought, because I already want to ask what else changed that day.
MAYA: You're going to be happy. We'll get there.
THEO: Good. Theory first?
MAYA: Theory first. Take N risk-neutral firms with independent private costs. The buyer announces a preselection number n, the count of firms that advance. Each firm submits a binding opening bid, and the n lowest go through. If n equals N, there's no preselection at all.
THEO: Then a descending auction among the survivors.
MAYA: Right. Starting from the lowest opening bid. And the paper measures what they call savings: the reserve price minus the price actually paid, which I read as a share of the reserve price. That splits into savings from the first stage and savings from the main auction.
THEO: Competitive benchmark first. What does preselection do to honest bidders?
MAYA: Here's a clean result. Under competition, removing preselection changes neither firm profits nor total savings. A revenue equivalence result. Bidding just shifts between the two stages.
THEO: So in the baseline model, preselection is neutral for honest firms.
MAYA: Neutral. Which sets up the punchline. Now introduce a partial cartel: a group of firms that coordinates and acts as one entity, knows its members' costs, and procures through its lowest-cost member. The rest of the firms are competitive.
THEO: How many members does it need for the trick?
MAYA: At least n. And fewer than N. If the cartel is smaller than the number of slots, it can't fill them. If it's everyone, there's no one left to exclude.
THEO: So the interesting zone is a cartel that's big enough to occupy every slot, but not the whole market.
MAYA: Yes, and in that zone the optimal strategy is what the authors call close bidding. At least n cartel members submit the same opening bid, and that common bid is low enough that competitive rivals get squeezed out with positive probability.
THEO: Why identical bids? Why not just bid low?
MAYA: That's my reading of the logic, not a quote. What matters is that at least n members sit below the rivals, and bidding the same number means no member has to undercut another.
THEO: And then in the main auction?
MAYA: If the rivals are shut out, nobody outside the cartel is pushing the price down. The cartel's own opening bid is basically what you pay.
THEO: That's collusion by exclusion. You don't rig the main auction, you rig who's allowed in.
MAYA: Exactly the title. And there's a clean comparative static. Removing preselection strictly lowers cartel profits and raises savings when the cartel size is between n and N minus one. Otherwise it leaves them unchanged.
THEO: So the model gives you a sharp prediction about who should be hurt by the reform.
MAYA: It gives three. One, within a preselection regime, cartel members bid close together often, and they don't compete with each other later. Two, once preselection is gone, cartel firms should be less likely to show up together in the same auction. Three, the gap in savings between collusive and competitive auctions should be larger with preselection.
THEO: One caveat on the theory. This relies on the cartel being, in the paper's words, strong.
MAYA: Yes. Acting as a single entity, knowing members' costs, ignoring side transfers. They say real cartels may be weaker or play suboptimally.
THEO: And they extend it somewhere, right? Entry costs, cost updating?
MAYA: In an appendix. Close bidding still marks a cartel there. But the effect of removing preselection is no longer clean in closed form, so it's not fully pinned down.
THEO: That matters, because in the real world preselection exists partly to save bidders the cost of competing. A model without entry costs will overstate the case against it.
MAYA: Hold that for the policy discussion. Let's go to the data.
THEO: Where do the opening bids come from?
MAYA: Administrative data from the Slovak electronic system. The key variable is the opening bid in each auction, normalized so you can compare across contracts of different sizes.
THEO: And the marker?
MAYA: The theory says cartel members should submit nearly identical opening bids. So the auction-level marker is close bidding: at least three normalized opening bids within one tenth of one percent of each other.
THEO: That's tight.
MAYA: Very tight. Before the reform, about nineteen percent of auctions with at least three bidders show close bidding. Weighted by contract value, it's about thirty-five percent.
THEO: Okay, but is nineteen percent a lot? Honest bidders can bunch.
MAYA: The authors ask that directly. Under a competitive benchmark, they find close bidding should show up in only about one point four percent of auctions on average.
THEO: So nineteen versus one and a half. That's not subtle.
MAYA: And they add that in a large share of auction groups, defined by product category and number of bidders, the difference is statistically significant at the one percent level.
THEO: Then the firm-level flag. How do you go from auctions to firms?
MAYA: For each firm with more than ten pre-reform auctions, they compute its share of close bidding in triples. A firm is flagged as a potential colluder if that share is above the ninetieth percentile. That works out to close bidding in at least about a fifth of its auctions.
THEO: So a percentile cutoff, not a legal standard.
MAYA: Right, and the authors are explicit. The marker is statistical evidence, not proof. Using it, they flag a hundred seventy-one of about four thousand one hundred twenty-two bidders. Roughly four percent.
THEO: Four percent of firms. How much activity is that?
MAYA: Those firms took part in about twenty-one percent of pre-reform auctions, and nearly thirty percent by contract value.
THEO: Concentrated but not tiny. Okay, now the part I care about. How do you know the flag means anything?
MAYA: Three validations. First, an actual conviction. In May twenty twenty-one, the Slovak Anti-Monopoly Office convicted six firms of bid rigging on two hundred seventy-six auctions between twenty fifteen and twenty seventeen.
THEO: And the data cover most of those.
MAYA: Two hundred seventy-four of the two hundred seventy-six. The marker, which is derived from the theory, identifies five of the six convicted firms.
THEO: I'd want to know about the one it missed.
MAYA: The paper says it took part in only ten of the two hundred seventy-six auctions and won once, a contract worth about five thousand nine hundred euros. The most active cartel member won more than nine hundred thousand euros.
THEO: So the miss is a marginal member. That's reassuring, but I'll say it plainly. It's one cartel, six firms. Five of six is encouraging, not a false-positive rate.
MAYA: Agreed, and they don't claim otherwise. There's no way to estimate false positives from a single case.
THEO: What's the second validation?
MAYA: Network structure. If these flagged firms are colluding in groups, then they should close-bid mostly with each other and not with competitors. The paper shows exactly that: triangle-like clusters of flagged firms, and flagged firms close-bid mainly with other flagged firms.
THEO: That's nice because a pure noise story wouldn't produce clustering.
MAYA: Right. And the third validation is the mechanism itself. Does the main auction look less competitive when flagged firms fill the slots?
THEO: Show me.
MAYA: Take auctions with at least three flagged firms where rivals ended up excluded. The cell is small, about five hundred auctions. There, the average number of bidders actually active in the main auction is about zero point four five, and the average number of bids is about two.
THEO: Versus?
MAYA: In the other cells with flagged firms, roughly one point three to one point five bidders and seventeen to twenty bids.
THEO: So the main auction essentially disappears.
MAYA: Almost entirely. And in regressions with controls, the drop in competition is concentrated in exactly those cases where flagged firms fill the slots. Having three or more flagged firms without excluding rivals doesn't reduce competition.
THEO: And they check that competitive bidders aren't just changing their own opening bids?
MAYA: They report that rivals' opening bids don't differ with cartel presence, so the effect isn't driven by rivals reacting.
THEO: That's a good check. Okay. The reform.
MAYA: The reform. The first outcome is joint participation: how often does a firm face a flagged firm in the preselection stage? Before the reform, a flagged firm faces another flagged firm about sixty-five percent of the time. For a competitive firm, it's about nineteen percent.
THEO: Which already fits cartels showing up together.
MAYA: It does. After the reform, in a linear probability model with bidder fixed effects, the interaction of being flagged and being post-reform is about minus zero point two three.
THEO: Twenty-three percentage points less joint participation, on a base of sixty-five.
MAYA: Roughly. And there's a wrinkle I should flag. The text of my version mentions a slightly different figure than the table, so I'd treat it as roughly twenty to twenty-five points. The robustness specifications give coefficients between about minus point two and minus point three.
THEO: So a big drop, and the exact size depends on specification. Fine. And no differential exit?
MAYA: They check, and they don't find flagged firms leaving differently after the reform. And the event study shows the drop right after the reform, with the same pattern if flagged firms are defined only from auctions before August twenty sixteen.
THEO: That last one is the check I'd have demanded. Otherwise you define cartel members using the same period you then compare against, and some of the effect is regression to the mean.
MAYA: Right. Defining them from earlier data separates the two.
THEO: Now savings. This is the part where a policymaker leans in.
MAYA: Before the reform, about two thirds of total savings came from the preselection stage. After, the shares swap. Competition moves from the first stage to the main auction.
THEO: And the headline?
MAYA: The savings gap between collusive and competitive auctions. Before the reform, auctions with flagged firms had savings roughly five and a half points lower than other auctions, off an average around fourteen percent.
THEO: So about forty percent below.
MAYA: Roughly. The introduction states the gap as about five point seven, falling to about three point five. The later regression says the interaction term is about plus two points. Either way, the gap closes by something like two points, close to forty percent of the original.
THEO: Let me restate. Take away preselection, and the damage cartels do to savings shrinks by about forty percent.
MAYA: That's the finding. But there's a second half, and I think it's the most honest part of the paper. Overall savings did not rise.
THEO: Why not?
MAYA: Because savings in competitive auctions fell slightly after the reform. The authors say that doesn't refute earlier literature on two-stage auctions.
THEO: So the reform helped on the cartel margin, and savings in honest auctions slipped. I'd be careful about reading that as a cost of removing preselection per se, given the other rule changes.
MAYA: Yes. And they put euro numbers on it, with a big warning that it's illustrative. In the year before, about two hundred sixty-three million euros of contracts were published on the system. About seventy-eight million went through auctions with flagged bidders. Procurers paid roughly sixty-seven million, saving about eleven million.
THEO: So removing exclusion would add how much?
MAYA: About one point six five million euros. But the across-the-board decline in savings subtracts about one point five seven million.
THEO: So the net is?
MAYA: About eighty thousand euros. The authors say the two effects cancel almost perfectly.
THEO: That's a striking result. A reform that does exactly what the theory predicts on the cartel margin and nets out to roughly nothing.
MAYA: And the paper also looks across sectors. The sectors where cartel-related distortions were largest before the reform are the ones where the reform recovered the most. The correlation is about minus point five seven.
THEO: Which suggests targeting. Remove preselection where it's being abused.
MAYA: That's the direction of the policy argument. Now let's do threats, because I know you've been holding some.
THEO: Several. First one, and it's the one I mentioned. The reform wasn't just removing preselection.
MAYA: Correct. It also added a double-confirmation rule for bids differing by more than ten percent, and it disabled bid retractions.
THEO: So any change in behavior after February twenty seventeen could come from those too.
MAYA: The identification leans on a difference: flagged firms versus others, before versus after. A rule change that affects everyone equally washes out in that difference. The authors list the retraction rule as a possible concern for bidding behavior.
THEO: But if flagged firms are the ones who use retractions strategically, a differential effect could leak in.
MAYA: Possible. The prediction that joint participation falls specifically is what's hard to attribute to retractions. But I wouldn't say it's fully ruled out.
THEO: Second. The marker comes from the same theory that makes the prediction. Is there circularity?
MAYA: There's some. The marker is built from the model, and then the reform effect on marked firms is a model prediction. What breaks the circle is the validation against the conviction, the network clustering, and the fact that the rival-opening-bids check goes the right way.
THEO: But the conviction is one case. And a second possibility is that these aren't cartels at all, but one owner with several shell companies.
MAYA: The authors take that on directly. They find no differential exit after the reform. Flagged firms have lower average sales, about three and a half million euros versus about nine million for the others, but similar size distributions by employees. And about eighty-two percent of pre-reform bidders could be matched to the financial statements register.
THEO: Which doesn't prove they aren't shells, but it makes a shell story less likely to be the whole thing.
MAYA: And economically, a shell group would be mimicking a cartel's behavior anyway. The difference is mostly legal.
THEO: Fair. Third. Sample size on the conviction side. I saw only a couple hundred auctions.
MAYA: Two hundred seventy-four auctions in the data, according to the table notes about two hundred fifty-one before the reform and twenty-three after. So post-reform comparisons within the convicted set are cautious.
THEO: Fourth is external validity. Slovak e-auctions for standardized goods, contracts between five thousand and a hundred thirty-five thousand euros, three advance to the main stage.
MAYA: The authors say don't generalize into a one-size-fits-all rule. It's a setting where agencies can't choose the format, which is clean for identification but narrow.
THEO: And fifth, adaptation. If agencies use the marker, cartels can avoid identical bids.
MAYA: The authors address this. They suggest agencies avoid publicizing the details, and argue that even if cartels adapt, less close bidding would still reduce the harm.
THEO: Because spreading the bids costs them some of their exclusion power.
MAYA: That's the argument.
THEO: Where does this sit in the literature?
MAYA: The related work on cartel detection in first-price auctions finds skewed bids and what Chassang and coauthors call missing bids. This paper's contribution is to say that in a two-stage auction, close bids can be exactly what an unconstrained cartel wants.
THEO: Different mechanism, different signature.
MAYA: Right. And on the policy side, they note restricted procedures are widespread. They cite evidence that restricted procedures made up over half of contracts in the U K and over a fifth in Denmark and the Netherlands in the period around two thousand eight to twelve.
THEO: So the question isn't niche.
MAYA: Not at all. The paper cites public procurement as about twenty-nine percent of government spending in O E C D countries, and about twelve percent of G D P.
THEO: Let me give my read. The theory is elegant and the prediction is crisp: close bidding, joint participation, and a savings gap that all move with the preselection rule.
MAYA: And the empirical side?
THEO: The marker passes a meaningful test with the conviction, the clustering, and the pre-August placebo-style definition. I'd still treat the flagged firms as suspects, not defendants. And I'd want a second convicted cartel before leaning on the five-of-six number.
MAYA: What about the reform design?
THEO: Good, not airtight, because of the bundled rule changes. But the differential structure and the specificity of the joint-participation result carry a lot of weight.
MAYA: What would you want next?
THEO: Two things. Variation in the preselection number rather than one reform, so you could trace the dose response. And a version where entry costs are explicit, because that's the benefit side of preselection that the model leaves out.
MAYA: I'd add data from another country with a similar format.
THEO: And the practitioner takeaway?
MAYA: Three points. First, preselection has an overlooked cost: it can hand a partial cartel a cheap way to exclude rivals. Second, you can screen using only opening bids. Look for clusters of nearly identical bids among a group of repeat firms. Third, don't mandate one format everywhere. The paper's own numbers show a reform that fixes the cartel problem can cost you elsewhere.
THEO: Agencies should keep discretion, and use screens like this to decide where to use preselection.
MAYA: Exactly. And the authors suggest future work on conditioning preselection on the close bidding you observe in the first stage.
THEO: One line?
MAYA: A rule meant to keep the auction competitive can be what lets a cartel keep it uncompetitive.
THEO: Good place to stop.
MAYA [warm]: Thanks for listening. The full citation and a link to the paper are in the show notes, along with what I read and what I didn't.
