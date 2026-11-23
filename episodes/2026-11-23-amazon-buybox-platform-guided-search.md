---
title: Is Amazon's Buy Box self-preferencing? Lee & Musolff (Econometrica 2026)
date: 2026-11-23
status: ready
paper: Lee, K. H. and Musolff, L. (2026). Two-Sided Markets Shaped by Platform-Guided Search. Econometrica 94(6), 2081-2115. DOI 10.3982/ECTA22288.
link: https://doi.org/10.3982/ECTA22288
sources_read: the full published Econometrica article (November 2026, pages 2081-2115) from the Econometric Society's open PDF, essentially complete text including conclusion, read via automated extraction in several passes; the online supplement and the Zenodo replication package were not read
summary: A structural study of Amazon's Buy Box using proprietary seller-side data. About ninety-five percent of consumers look only at the featured offer, the algorithm favors Amazon's own offers, and yet the authors' counterfactuals say that favoritism is roughly consumer-surplus maximizing, because consumers also like Amazon's offers.
caveats: Every figure comes from automated extraction of the published article and is given approximately where the extraction was ambiguous: some table columns were misaligned, the demand elasticity appears as about minus fourteen (table value about minus thirteen point seven), the counterfactual price decline and entry increase appear as the same three percent figure and may be a typo, and the text says GMM while a table says SMM for the cost estimates. The data end in March 2020, Amazon's own sales are not observed, and the authors assume Amazon's retail arm maximizes short-run profit and that consumers and merchants do not multihome. The counterfactual benchmark is a modeling proxy for a cheapest-offer-only rule. Not covered: the online supplement, the replication code, and any reading of the working-paper versions.
---
# Script for a ~20 minute episode. Numbers only from the published Econometrica article (Lee and Musolff, Nov 2026). Style in [brackets]; <short pause> and |backchannels| are Gemini TTS markup.

MAYA [curious, conversational]: Here's the number that stopped me in today's paper. Ninety-five percent. That's the estimated share of Amazon shoppers who only ever look at the single offer sitting in the Buy Box.
THEO: Ninety-five. So five percent compare everything, and everyone else takes what they're shown.
MAYA: Roughly, yes. And that number drives the whole paper, because if almost nobody looks past the Buy Box, then whoever decides what goes in the Buy Box has enormous power.
THEO: Which is exactly what regulators worry about. Amazon picks the winner, and Amazon is also a seller in the same market.
MAYA: Right. The paper is Two-Sided Markets Shaped by Platform-Guided Search, by Kwok Hao Lee and Leon Musolff. It's in Econometrica, the November twenty twenty-six issue, volume ninety-four, number six. I'm working from the full published article.
THEO: And the verdict? Is Amazon rigging the box?
MAYA: Here's the headline, and it isn't what the policy debate prepares you for. The algorithm does favor Amazon's own offers. But the authors argue that this favoritism does not hurt consumers, because consumers also prefer Amazon's offers. <short pause> In their counterfactuals, consumer surplus is about as high as it can get at the favoritism the algorithm actually applies.
THEO [skeptical]: Okay. That's a strong claim about a company that's currently being sued over exactly this. I'm going to push on it.
MAYA: Good, because it rests on a chain of identification choices, and we should walk through them. Setting and data first.
THEO: Go.

MAYA: Some background. Amazon lets third-party sellers list offers right next to its own. The paper cites Amazon's own figures: about one point nine million merchants used the marketplace in twenty twenty, and third-party listings were about sixty percent of sales.
THEO: |Mm-hm.| So the marketplace isn't a side business.
MAYA: Not at all. Now, when a product has several offers, Amazon features at most one of them, the Buy Box. It's the same featured offer for every shopper. The paper drops a rare case where Amazon features two, one for Prime members and one for everyone else.
THEO: And how much of the sales go through that box?
MAYA: Estimates differ. The paper notes a Senate Judiciary Committee figure of around eighty percent in twenty twenty, and a twenty twenty-three F T C and state attorneys general figure of nearly ninety-eight percent.
THEO: That's a big gap, and your model should land somewhere in it.
MAYA: They check that. Hold the thought.
THEO: Okay. What's the data?
MAYA: Proprietary data from a repricing-service company, pulled through Amazon's own interfaces. A repricing service changes a seller's price automatically as competitors move, so the authors see the market from the seller's side. The period runs from late August twenty eighteen to late March twenty twenty. There are about nineteen point four million records of which offer got featured, around eight hundred thousand sales, roughly forty-seven thousand products and sixty-three thousand merchants.
THEO: And here's what's missing, I assume.
MAYA: Three limits. First, prominence is only recorded right after the set of offers changes. If Amazon rotates the box without any change, that isn't notified. Second, sales are observed only for the one merchant the repricing company serves in each market. Third, Amazon's own sales aren't observed, since Amazon isn't a client.
THEO [leaning in]: So how do they get from one merchant's sales to the demand facing the market?
MAYA: They convert sales ranks into monthly sales using an outside power-law model, and then into shopper arrivals using conversion rates for sponsored listings, roughly eleven to twenty-one percent.
THEO: I'll flag, as commentary, that's a lot of imputation under the demand side. We'll come back to it.

MAYA: Before the model, the descriptive facts, because they set up the puzzle. Who actually gets the box?
THEO: Cheapest, presumably.
MAYA: Only about forty-one percent of the time is the featured offer the cheapest, and about twenty-six percent of the time it's the second cheapest. It's offered through F B A, Fulfilled by Amazon, about eighty-six percent of the time.
THEO: So fulfillment matters a lot.
MAYA: Very much. And Amazon's own offer is featured about thirteen percent of the time overall. But look at the conditional number. In the roughly nineteen percent of observations where Amazon has an offer, it's featured about two thirds of the time, and in those cases Amazon is also the lowest-priced offer about forty-five percent of the time.
THEO: Hm. So Amazon wins often, but it's also often cheapest. That already muddies "self-preferencing."
MAYA: And the authors say that themselves. Being sold by Amazon is the strongest bivariate predictor of prominence, but they stress these are not causal. Higher prices, fewer feedback ratings and slower dispatch lower your chance. Still, an offer priced twenty percent above the minimum gets featured about seven percent of the time.
THEO: So price isn't everything, and it isn't nothing.
MAYA: There's one more descriptive fact I want, because it's quirky. Sometimes the platform cancels prominence, meaning the box is simply empty. And cancellation gets more likely as the cheapest offer's price climbs above the manufacturer's suggested retail price.
THEO [laughing]: That's a pricing cap by another name.
MAYA: The authors say it can discipline prices much like a most-favored-nation clause would, and the paper notes Amazon dropped those clauses in Europe by twenty thirteen and in the U S by twenty nineteen. But in the counterfactuals they assume every market has a featured offer, because an empty box would swamp every other welfare effect.

THEO: And the regression on Amazon's shadow?
MAYA: When Amazon has an offer, the observed merchant's sales fall sharply, and the effect shrinks with controls and offer fixed effects but stays negative and significant.
THEO: And there are two stories. Shoppers like Amazon, or the algorithm steers to Amazon.
MAYA: Exactly, which is why the authors build a structural model.

MAYA: Three pieces. Consumers, the prominence algorithm, and firms.
THEO: Consumers first.
MAYA: Shoppers arrive as a Poisson process. Each is one of two types. A fraction, call it rho, is sophisticated: they ignore what's featured, look at all the offers, and choose among them and an outside option with a nested logit. The remaining one minus rho are what the paper calls unsophisticated. They consider only the featured offer and the outside option.
THEO: And price enters relative to the M S R P, so a dollar matters more on a cheap item.
MAYA: Yes. Utility depends on price over M S R P and characteristics: F B A, being sold by Amazon, shipping time, feedback.
THEO: Now the algorithm.
MAYA: The authors model the Buy Box choice as a nested logit over the inside offers, with a separate nest for canceling prominence. Its weights are on the same kinds of characteristics, price relative to M S R P, F B A, Amazon, dispatch time, feedback. The random shocks stand for deliberate rotation or evaluation error. And that's why counterfactuals on the algorithm are framed as changing the weights it puts on goals.
THEO: And firms?
MAYA: Each market has a fixed entry cost and about fifteen potential entrants. A seller learns only its own marginal cost before entering, a kind of blind entry. After entry, sellers know their rivals and play Bertrand-Nash pricing. And here's the key bit: they internalize that their price affects whether they get featured. Sellers keep a share of revenue, because the platform takes fees.
THEO: And Amazon's offer?
MAYA: Taken as given on entry, and its price maximizes its short-run profit. That's a real assumption, and it matters for the self-preferencing question, so keep it in mind.
THEO: Noted. The model delivers a unique symmetric equilibrium in cutoff strategies, I think?
MAYA: Right. Sellers enter if and only if their marginal cost is below a cutoff. Proposition one in the paper.

THEO [sharper]: Now the part a referee would live in. Identification. How do you get from one merchant's sales to "ninety-five percent only look at the box"?
MAYA: Two ingredients. One is the model's structure. The other is an instrument.
THEO: Instrument for what?
MAYA: For prominence. Because the observed prominence in the data can be stale, remember, high-frequency reassignments aren't recorded. That's measurement error, and it biases you toward thinking prominence doesn't matter much.
THEO: Classic attenuation.
MAYA: Right. And you can see it in the numbers. Using observed prominence, the estimated sophisticated share is about seventy-one percent. Using the instrument, it drops to about five percent.
THEO: Wow. That's the whole ballgame.
MAYA: It is. The instrument is prominence eligibility. To be eligible you need a professional seller account, at about forty dollars a month, and Featured Merchant status. The instrumented prominence probability is eligibility times the model's predicted probability. The first-stage F-statistic is reported as about eighty-three hundred.
THEO: So the exclusion restriction is that eligibility moves sales only through the box.
MAYA: Yes, and the authors acknowledge the risk. If eligibility also reflects something consumers value, like a reputation for on-time delivery that isn't in the data, the restriction fails. They argue that's unlikely.
THEO: |Hm.| I'd want more on that. Eligibility criteria are probably correlated with seller quality that shoppers can see on the page.
MAYA: Well, shoppers see a lot of that on the page, and the paper controls for those characteristics: feedback count, shipping time, F B A. But I take your point. It's the load-bearing assumption.
THEO: What about Amazon's preference, the consumer taste for Amazon?
MAYA: Identified from that shadow effect we discussed. If an Amazon offer's presence lowers the observed merchant's sales even after accounting for the algorithm's prominence, that's read as consumers genuinely preferring Amazon.
THEO: And the threat is that Amazon enters markets selectively.
MAYA: The authors flag exactly that. If Amazon enters markets with negative demand shocks, its preference is overstated; if it enters positive-shock markets, it's understated. Same for substitutability confounds.

THEO: What else are they assuming?
MAYA: Main specifications set unobserved quality to zero, in both the algorithm and demand. As robustness they allow time-invariant unobserved quality with offer fixed effects. For the algorithm, the price coefficient changes only modestly. For demand, sales are sparse, so fixed effects mostly identify substitution to the outside option, and they reduce the estimated price sensitivity.
THEO: That second one is a bit uncomfortable for the demand side.
MAYA: It's a limitation they state.

MAYA: Okay, results. The algorithm first.
THEO: How price-sensitive is the box?
MAYA: Very. The implied price elasticity of prominence is about minus twenty-one in the preferred specification. In elasticity terms, a one percent higher price cuts your chance of being featured by roughly twenty percent.
THEO: And F B A?
MAYA: Worth about a twelve percent price advantage. Being sold by Amazon adds roughly another four and a half percent on top of F B A. The paper summarizes it this way: Amazon's offers are featured about as often as similar offers priced about five percent cheaper.
THEO: So the favoritism is real but not huge.
MAYA: Real, moderate. For scale, a one-day-longer dispatch time carries a penalty similar to Amazon's advantage. And in relative terms, Amazon's weight in the algorithm is about zero point three nine times the weight on F B A.
THEO: Now demand. What do shoppers want?
MAYA: Here's the pleasant surprise. In demand, being sold by Amazon is worth about one point one two times F B A. So the algorithm weights Amazon less than F B A, about zero point four times, while consumers value it slightly more than F B A.
THEO: So in the language of the paper, the algorithm under-weights Amazon relative to what consumers want?
MAYA: Relative to F B A, yes, in these estimates. I'd be careful, it's the paper's estimates, but that's the logic behind their conclusion.
THEO: And the price elasticity of demand?
MAYA: About minus fourteen when prominence responds to price. But about minus one if prominence is held fixed. That gap is the ninety-five percent again. Almost all the price sensitivity a seller faces comes through the box.
THEO: Meaning a price cut is mostly a bid to win the box.
MAYA: Exactly. And that's why the algorithm's price sensitivity is such a powerful lever.

THEO: Okay, but the validation. You said hold that thought.
MAYA: Right. The paper estimates the share of sales going through the Buy Box and compares it with regulators' figures. The naive maximum-likelihood estimate is about forty-two percent. The estimate with the eligibility instrument is about ninety-six percent in the structural model, and about ninety-one percent in a linear version.
THEO: Versus ninety-eight from the F T C.
MAYA: And the European Commission's twenty twenty-two figure for France and Germany, in the seventy to ninety percent range. The authors call the structural estimate very close to the F T C number.
THEO [dry]: I'd call that a consistency check, not a validation. The naive version being forty-two should tell you how much the instrument is doing.
MAYA: The paper itself describes it as consistency, and it notes the comparisons use different countries, years and definitions. The ninety-five percent isn't tested directly, that's the honest reading.
THEO: And costs?
MAYA: Amazon's marginal costs come out significantly lower than third-party sellers', and fixed costs are small, with an interquartile range of roughly thirty-seven cents to two dollars and eighty-three cents per product-month.

THEO: Now the counterfactuals. This is where the policy bite is.
MAYA: Three experiments. First, the value of search guidance. What if the platform didn't guide unsophisticated shoppers at all?
THEO: Meaning what?
MAYA: The benchmark is that unsophisticated consumers just consider the cheapest offer. It's implemented by tripling the price coefficient and switching off non-price characteristics. So it's a proxy for a cheapest-offer rule, not a literal one.
THEO: That's a design choice I'd want to hear defended.
MAYA: It's a simplification, and the paper says the tripling is partly for convergence reasons. Now the results, per the paper. In the short run, where prices and entry are fixed, consumer surplus rises about nineteen million dollars, or one point seven percent, from guidance. In the long run, with prices and entry adjusting, about twenty-nine million, or two point six percent. Welfare rises about thirty-two million in the long run.
THEO: Out of a sample of how big?
MAYA: About forty-seven thousand products and roughly a hundred sixty-one million dollars in revenue. Sales per product rise by about one point seven per month in the short run and two point five in the long run. And in the long run the mean minimum price falls about three percent, with entrants up about three percent.
THEO: I'll note the extraction gave me the same three percent twice. Do we trust that?
MAYA: Honestly, I'd treat both as approximately three percent. It might be a coincidence, or a typo in the text. The qualitative point is the same: guidance brings more entry and lower minimum prices, mostly because it matches people to offers with attributes they like, F B A, fast shipping.
THEO: So guidance isn't just steering, it's matching.
MAYA: That's the authors' interpretation, yes. Second experiment: how price-sensitive should prominence be?
THEO: Amazon takes a percentage of revenue, so you might think it wants higher prices.
MAYA: The authors raise that worry. But the current price sensitivity is approximately optimal for long-run consumer surplus. Make the box more price-sensitive and you lose matching on quality and, in the long run, reduce entry. Make it less price-sensitive and consumers are hurt more sharply through higher prices, while Amazon's profits rise dramatically. The paper notes Amazon did not choose such a low price weight in the sample period.
THEO [skeptical]: Which I'd call a fact about the sample period. The paper itself says Amazon can change its algorithm at will.
MAYA: Fair. Third experiment, the title question. Is Amazon self-preferencing?
THEO: What do they vary?
MAYA: The weight on Amazon's own offers relative to the F B A weight, starting from the status quo of about zero point three nine. Across the range they consider, Amazon's share of the box on products where it has an offer runs from about sixty-two to eighty-seven percent.
THEO: And?
MAYA: In the short run, consumer surplus rises with more weight on Amazon, and only reverses at about five point six times the F B A weight. In the long run, consumer surplus peaks at about half the F B A weight. That's, in the authors' words, just slightly above the status quo. After that, higher prices bite.
THEO: So it's near the status quo.
MAYA: Exactly. And that's why the abstract says consumer surplus is roughly maximized at the estimated Amazon advantage.
THEO: And who loses?
MAYA: Third-party sellers. Their preferred weight on Amazon's offers is zero. Amazon gains more profit from more weight, especially in the long run. Consumers are roughly neutral near the status quo.
THEO: Which is itself a policy question. A consumer-surplus standard says fine. A standard that cares about sellers, or about Amazon's profits, says maybe not.
MAYA: Right, and the authors frame self-preferencing as a matter of degree. Featuring Amazon's offers more raises prices but has little effect on entry in their model. They say the data give no support for the idea that it's a barrier to entry.

THEO: Okay. Now my skeptic's list. What would change the conclusion?
MAYA: Let me start with what the authors are candid about. Data end in March twenty twenty, and Amazon can change its algorithm. They proxy market size. They don't observe Amazon's sales or total arrivals. And they say the model doesn't explicitly allow multihoming by consumers or merchants, though the entry margin implicitly captures merchants leaving.
THEO: What about the self-preferencing channels they don't model?
MAYA: Good one. The self-preferencing experiment is about the Buy Box weight. The paper's counterfactuals don't model other channels, search ranking is the obvious one, and they assume Amazon's retail arm maximizes short-run profit. Long-run supply-side effects, merchant quality, investment, innovation, are listed as open.
THEO: And F B A.
MAYA: The paper leaves open how prominence algorithms affect F B A adoption, whether it eventually raises prices or improves service. That's a real open question, since F B A is such a big input into who wins.
THEO [leaning in]: Let me add my own worries, as commentary. One, the five percent sophisticated share is identified off an instrument and imputed arrivals. A modest change there changes how much of Amazon's advantage looks like steering versus taste.
MAYA: The authors say it directly: underestimating the unsophisticated share would misattribute prominence advantage to consumer preference.
THEO: Two, the welfare standard counts shoppers' purchases, not the shoppers who might have bought something better if the box showed them different options. If ninety-five percent only see one offer, are those revealed preferences?
MAYA: That's a deep one. The model treats choices conditional on what's shown as preferences. The authors don't claim to separate which consumers benefit from guidance and which are harmed, and they say richer sales data could show how much people value faster shopping versus better choices.
THEO: And three, the modeling choices on the counterfactual benchmark.
MAYA: Right, the tripled price coefficient. It's not a literal cheapest-only rule.
THEO: Still, I'd say it's a more careful paper than the usual claim on either side.

MAYA: Let me place it in the literature, as the paper describes it. The closest papers are Farronato, Fradkin and MacKay, from twenty twenty-five, who find consumer surplus would fall if Amazon's own brands were removed from search, and Raval from twenty twenty-two, who finds Buy Box steering toward Amazon. This paper adds a welfare analysis using sales data, plus the long-run entry margin.
THEO: What would an agency economist take from it?
MAYA: My reading: prominence skew alone isn't evidence of harm. The question is what consumers would choose if they compared everything. The paper's contribution is a way to ask it.
THEO: And my caution is the other way. This is one platform, a period ending before the pandemic shopping surge, and estimates that depend on an instrument. So I'd use it as a framework and a benchmark, not as a verdict for a courtroom.
MAYA: Both fair.

MAYA [warm]: So, one line. Amazon's Buy Box really does steer, ninety-five percent of shoppers follow it, and it does favor Amazon, but in this paper's model that favoritism is close to what maximizes consumer surplus, while third-party sellers would prefer none.
THEO: And the caveat I'd attach: it's a consumer-surplus answer on a particular sample, through one channel, with a load-bearing instrument.
MAYA: Agreed. <short pause> That's it for this one.
