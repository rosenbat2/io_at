---
title: Is merger enforcement too lax? Bhattacharya, Illanes & Stillerman (AER 2026)
date: 2026-11-13
status: ready
paper: Bhattacharya, V., Illanes, G., and Stillerman, D. (2026). Merger Effects and Antitrust Enforcement: Evidence from US Consumer Packaged Goods. American Economic Review 116(8), 2996-3035. DOI 10.1257/aer.20240497.
link: https://doi.org/10.1257/aer.20240497
sources_read: the open NBER working paper 31123 (revision of August 2025), essentially the full text (main text, conclusion, most appendices), read via automated extraction; the published AER version was not read
summary: Across a broad sample of consumer packaged goods mergers the average price effect is near zero but the spread is wide. What that means for the claim that antitrust enforcement has been lax, and what an enforcement model says would happen under a stricter standard.
caveats: Every figure comes from the working-paper version and may differ from the published AER version. Ranges such as the average price effect and the counterfactual price declines depend on specification, so the episode gives them approximately. The authors' enforcement thresholds are estimated from only ten challenged mergers. Not covered in the text read: whether pack-size changes are handled.
---
# Script for a ~20 minute episode. Numbers only from NBER w31123 (Aug 2025 revision). Style in [brackets]; <short pause> and |backchannels| are Gemini TTS markup.

MAYA [curious, conversational]: Here's a number that sounds almost boring. <short pause> Across a big sample of consumer goods mergers, the average price change after the deal was somewhere between a six tenths of a percent decrease and a one percent increase.
THEO: Okay. So basically nothing. Which, if you think antitrust enforcement has been too lax, sounds like bad news for your argument. Or, wait. Is it?
MAYA: That is exactly the question. Today's paper is Merger Effects and Antitrust Enforcement, by Vivek Bhattacharya, Gastón Illanes, and David Stillerman. It's in the American Economic Review this year, and I'm working from the N B E R working paper version, revised in August twenty twenty-five.
THEO: |Mm-hm.| And the pitch, as I understand it, is that an average near zero can hide almost anything.
MAYA: Right. They find a small average but a huge spread across mergers. And then they use what agencies actually challenged to ask a second question: how strict are the agencies acting, and what would happen if they were stricter?
THEO: So two papers in one. A retrospective, and then a model of enforcement.
MAYA: Exactly. And the second part is what makes this more than another retrospective. We'll take them in order.
THEO: Before we dive in, why does the average matter so much here?
MAYA: Because of an old argument. The authors say they're responding to Carlton, in two thousand nine, who pointed out that a small average price change doesn't by itself show that agencies are being strict.
THEO: Because you only observe the mergers that were consummated. The ones the agency stopped, you never see.
MAYA: Right. So the average of consummated mergers is already filtered by enforcement.
THEO: Which is why I'd rather see the distribution than the mean.
MAYA: And the authors agree. Okay, let's start with the data.
THEO: Go.
MAYA: The deal universe comes from S D C Platinum, a database of mergers and acquisitions. They keep deals worth at least two hundred eighty million dollars that involve manufacturers of retail products.
THEO: So big deals. Not corner store roll-ups.
MAYA: Big deals, yes. For prices and quantities they use the Nielsen I Q retail scanner data, covering roughly thirty-five to fifty thousand stores and millions of distinct products, from two thousand six through two thousand eighteen.
THEO: Scanner data. So actual shelf prices, by product code and by city.
MAYA: By U P C and by D M A, which is the Nielsen media market. And because Nielsen doesn't tell you who owns a product, they bring in Euromonitor Passport to map products to owners.
THEO: How do they decide a deal counts? Plenty of acquisitions are in unrelated categories.
MAYA: They keep a deal if the two parties overlapped in at least one product market and D M A, so there's a real horizontal overlap. And the window runs from thirty-six months before the announcement to twenty-four months after completion.
THEO: So the unit is really a product market, deal pair.
MAYA: Right, that's what they call a merger here. They end up with one hundred twenty-nine mergers, drawn from forty-seven deals.
THEO: |Okay.| That's a lot more than five.
MAYA [dryly]: It is a lot more than five. That's the contrast with earlier retrospectives, like Ashenfelter and Hosken in twenty ten, which looked at a handful of mergers picked as the ones most likely to be problematic.
THEO: So instead of picking on the enforcement margin, this is closer to a census of the big overlapping deals.
MAYA: Closer, yes. With caveats. It's consumer packaged goods, only deals above that size cutoff, and only overlaps you can see in the scanner data.
THEO: And what about the mergers the agencies actually went after?
MAYA: They code that too. Six mergers, from four deals, had an agency propose a remedy for a horizontal concern. And four mergers, from two deals, were proposed and then withdrawn after concerns from the D O J or the F T C. So ten challenged mergers in total. None of them went to court.
THEO: Ten. That's thin.
MAYA: Hold on to that. It matters when we get to the enforcement model.
THEO: Okay. The core problem, then. How do you build the counterfactual price?
MAYA: Here's the design. Treatment is the merger completing, for the merging parties' products. Products of the non-merging competitors in the same market are tracked as a separate group, with their own coefficient.
THEO: Because rivals might react.
MAYA: Exactly. And the control group is the pre-merger period, for the same product, in the same city, at the same time of year.
THEO: So there's no outside control group. It's a within-product before and after.
MAYA: A before and after with a trend model. Step one: using the thirty-six pre-merger months, they regress log price on a brand-specific linear time trend, product by city fixed effects, month of year fixed effects, input cost series, and median household income.
THEO: And then they predict forward.
MAYA: Right. Step two uses the twenty-four post-merger months. They take the gap between the actual log price and the predicted one, and regress that gap on indicators for merging party and non-merging party. Doing it in two steps keeps the post-merger data from contaminating the pre-trend.
THEO: Hm. But the obvious question: why not use rivals as a control group? Standard difference in differences.
MAYA: The authors address that directly. Their main reason is that non-merging firms are competitors, so they may adjust their strategies in response to the merger, which would contaminate the counterfactual.
THEO: So rival responses are the thing you want to measure, not the thing you want to difference out.
MAYA: Exactly. They also reject two other options. Synthetic controls, or untreated markets, because it's hard to find donor markets that share the cost and demand shocks but aren't treated, and the estimates were sensitive to dropping single donors. And untreated geographies, which would drop thirty-nine of the hundred twenty-nine mergers, the national ones, and the untreated markets aren't random anyway.
THEO: Okay. So the identifying assumption is basically: absent the merger, the product's price would have kept on its pre-merger trend, given seasonality, costs, and income.
MAYA: Yes. And they run placebos. If you randomize the merger dates, the estimates center on zero and come out tighter than the real ones. The real dates show departures from trend that random dates don't.
THEO: That's reassuring about noise. It doesn't fully rule out a trend break that coincides with a merger for some other reason.
MAYA: No. And there's a footnote that makes an interesting point. A correlation between pre-trends and effects could reflect real industry dynamics, like a declining industry, and not only a failure of identification.
THEO: So the merger and the trend break could both be responses to the same underlying decline.
MAYA: Right. They flag it rather than solve it.
THEO: Okay. Results?
MAYA: The average price effect, across specifications, is between minus point six percent and plus one percent. In the baseline, the overall mean is point three percent. For the merging parties, point one percent. For non-merging rivals, point five percent.
THEO: So both small. Rivals actually go up a bit more than the merging firms.
MAYA: Slightly, yes. But now the spread. The standard deviation of the merger-level effects is between four and seven and a half percentage points, depending on the specification. In the baseline table it's around four and a half.
THEO: So a typical merger moves prices by more than four points in one direction or the other, around a mean near zero.
MAYA: And the quartiles make it concrete. A quarter of mergers lower prices by more than roughly two to three percent, and a quarter raise them by more than roughly three and a half percent.
THEO: Wow. Okay. So a big group of mergers that lowered prices, and a big group that raised them.
MAYA: And look at how the two groups move together. Thirty-six percent of mergers lower prices for both the merging firms and their rivals. Thirty-six percent raise prices for both. About thirteen percent lower the merging firms' prices but raise rivals', and fifteen percent do the reverse.
THEO: So seventy-two percent of mergers have the two groups moving in the same direction.
MAYA: And the correlation between merging and non-merging price changes is about point four nine. The authors read that as consistent with strategic complementarity. If the merged firm raises prices, rivals can profitably follow.
THEO: Though a common cost or demand shock the controls missed would look the same.
MAYA: Fair. That's the flip side.
THEO: What about timing? Do prices jump right away?
MAYA: There's an event study. Among mergers in the top price increase quartile, merging-party prices are roughly five percent higher five months after the merger.
THEO: So not instant, but it shows up within the first year.
MAYA: And the paper notes that cost synergies, which could push prices down, seem to take time to materialize, and that contract renegotiation with retailers may delay market power gains.
THEO: One thing I want to flag. These are retail prices, not wholesale. The merging manufacturer sets the wholesale price, and the retailer sets the shelf price. So pass-through muddies it.
MAYA: Agreed. That's a real limit.
THEO: And is that spread real? A standard deviation of point estimates includes sampling noise.
MAYA: They check. A Bayesian shrinkage exercise has limited quantitative effects, because the dispersion across mergers is much larger than the estimated standard errors.
THEO: Okay. And robustness on the average?
MAYA: Using the Nielsen consumer panel instead gives a mean of about seven tenths of a point. Restricting to food mergers moves the means up by a few tenths. Dropping mergers with divestitures has limited effect. So the sign of the average isn't pinned down.
THEO: Which is why the distribution is the real story.
THEO: Now quantities and assortment, because price isn't the whole story.
MAYA: Average quantity effects range from minus point four to minus one percent. Baseline, minus point five. But for the merging parties it's much bigger: about minus six point four percent on average. And sixty percent of mergers reduced total quantity.
THEO: Minus six for the merging firms but only half a percent overall. So rivals pick up volume.
MAYA: That's one natural reading. On assortment, the merging parties' store counts fall about two point seven percent on average, though thirty-eight percent of mergers actually expand their store networks. Brands sold per market fall about two point two percent for the merging parties and three point two percent for non-merging parties.
THEO: And I assume dropping brands is concentrated somewhere.
MAYA: Among small brands and small markets, yes.
THEO: So variety is a second margin that a price index alone would miss.
THEO: One open question for me. If a firm shrinks the package, a flat price per U P C hides a price increase. I'm not sure the paper addresses pack sizes, so that's worth checking.
THEO: Okay, now the part antitrust lawyers will care about. Do the merger guidelines' structural presumptions predict price increases?
MAYA: They test it. As a reminder, the twenty ten guidelines' red zone is a change in H H I over two hundred, with a post-merger H H I over twenty-five hundred. The twenty twenty-three guidelines presume harm if the change in H H I is over one hundred, and either the post-merger H H I is above eighteen hundred, or the merging firms' share is above thirty percent.
THEO: And the finding?
MAYA: Positive, but modest. A one hundred point increase in the change in H H I goes with about a two tenths of a percentage point higher price change for the merging parties, three tenths for non-merging parties. Merging share above thirty percent goes with larger price effects, roughly two point seven points for merging parties.
THEO: Those are small coefficients. I'd guess the R squared is tiny.
MAYA: Low for all the specifications, yes. And interestingly, the level of H H I is negatively correlated with merging-party price changes, which the authors attribute to selection.
THEO: Which is the theme. What gets proposed and approved isn't random.
MAYA: Right. And they report that correcting for approval selection strengthens the change in H H I correlation and makes the level of H H I insignificant.
THEO: So change in concentration matters, and level doesn't once you correct for selection.
MAYA: That's what they report. And one more. In their probability analysis, mergers with a change in H H I above roughly one hundred seventy-five, or a merging share above roughly twenty percent, are more likely than not to raise merging-party prices.
THEO: Twenty percent share is below the thirty percent in the twenty twenty-three guidelines.
MAYA: It is. In their data, a lower share cutoff looks informative, but with the noise caveat.
THEO: Okay. So that's the retrospective. Now the second half, which is the part I'm more skeptical about, because it's a revealed preference exercise.
MAYA: Right. Here's the model. The agency gets a noisy signal of a merger's price effect, combines it with a prior centered on market structure, and challenges when the expected price increase exceeds a threshold. The paper estimates that threshold from which mergers were actually challenged.
THEO: So when the abstract says agencies act as if.
MAYA: It means they act as if they challenge mergers they expect would increase prices by more than four point eight to six point three percent.
THEO: That is pretty high. A merger expected to raise prices five percent clears the bar.
MAYA: Under their estimates, yes. Their sales-weighted aggregate threshold is around five to six point three percent depending on the specification, and in the counterfactual section the current average is about six percent. And at that threshold, the chance that a given merger is challenged is about seven and a half percent.
THEO: And that's estimated off ten challenged mergers.
MAYA: Right. And the appendix says the threshold estimates are noisy.
THEO: So I wouldn't hang my hat on four point eight versus six point three.
MAYA: No. The order of magnitude is the point. Several percent, not one or two.
THEO: Okay. What are the counterfactuals?
MAYA: If you lowered the threshold to two point five percent, the challenge probability rises to about thirty percent. Roughly four times as many challenges.
THEO: So the agencies would need to challenge about four times as many mergers.
MAYA: Right. And the benefit: the average price change of consummated mergers falls by somewhere around one to one and a half percentage points, depending on the specification.
THEO: That's on a baseline average of about zero.
MAYA: Right, so it turns a roughly zero average into an average decrease. And if you went all the way to a zero threshold, sixty to seventy percent of consummated mergers would have price decreases, but agencies would be challenging more than half of all mergers.
THEO: And what do you give up? Type one errors, blocking good mergers?
MAYA: Here's the interesting result. Type one errors are infrequent at the current threshold, and only become non-trivial around a three percent threshold. At the extreme of a zero threshold, about ten percent of blocked mergers would be type one errors.
THEO: And type two errors, letting bad ones through?
MAYA: Around half of allowed mergers involve type two errors at the current threshold. That falls to about thirty-five percent at a two point five percent threshold.
THEO: So the headline policy claim is that current enforcement rarely blocks pro-competitive mergers but lets through many anticompetitive ones, and modestly tighter standards would help without many more type one errors.
MAYA: That's their conclusion. And the main cost is agency burden. The workload rises significantly, unless stricter standards also reduce how many mergers get proposed.
THEO: And that's where the assumptions bite.
MAYA: Let's walk through them. The agency observes a noisy signal of each merger's price change, with noise estimated from the data. The agency challenges when the expected net benefit exceeds a challenge cost. And the cost of allowing a merger is proportional to the price change, so the objective is price based.
THEO: So no weight on innovation, quality, labor markets, anything non-price.
MAYA: Right. The paper says unobserved non-price concerns bias the noise estimate upward, so the agency's signal is probably more precise than the model suggests. Next, challenges succeed with probability one, though an appendix relaxes that.
THEO: And I'd guess they assume the set of proposed mergers doesn't change when the threshold moves.
MAYA: Yes. Selection into proposal doesn't change with the threshold. And the authors say what that implies. If laxer thresholds induce worse mergers, the price effects are lower bounds. If stronger thresholds deter proposals, the burden estimate is an upper bound.
THEO: So deterrence cuts in favor of tighter standards, in their own framing.
MAYA: Yes, in their own framing. A few more caveats. Divestitures are treated as lower bounds on the true price change. Agency price predictions usually exclude synergies. And the appendix says external validity is a concern, because the industries differ and agencies may not use the same decision rule across industries.
THEO: Let me push on the revealed preference part. When we say agencies act as if the threshold is six percent, that isn't a statement about what they believe or intend.
MAYA: Right. It's the threshold that best rationalizes their challenge pattern, given the model. Litigation risk, budgets, politics, the model reads all of it as one number.
THEO: And lowering the threshold in the model is a clean change. In reality, to challenge four times as many mergers, you need staff, and you need to win in court. The model has challenges succeed with certainty, and none of these mergers went to litigation.
MAYA: So it's an estimate of what agencies would do if they acted on their signals more aggressively, not what would happen if the law changed. That's a fair summary.
THEO: One more link back. The earlier retrospectives, like Ashenfelter and Hosken, picked mergers on the enforcement margin. This broad sample gives a different picture: near zero on average, wide dispersion.
MAYA: Which means one merger's retrospective tells you very little about the next. And the structural screens, the change in H H I and merging share, have some predictive power but a low R squared. As far as I can tell, the paper compares them to enforcement through correlations, and doesn't simulate a pure structural rule against what agencies do.
THEO: Let me give my overall read. The retrospective part is credible and valuable. A broad sample, scanner data, a transparent before and after design, with candid discussion of what the design can't do.
MAYA: And the enforcement part?
THEO: It's an interesting structural lens, and it's honest about its assumptions. But the headline numbers come from ten challenged mergers and a price-only objective, and I'd treat the thresholds as an order of magnitude, not a point estimate.
MAYA: I'd add one thing. The central message survives that critique. Even if you shade the threshold estimates, the average of consummated mergers hides a wide dispersion, and a lot of price-increasing mergers got through.
THEO: And that rebuts the idea that a small average means enforcement is about right.
MAYA: Right. A small average is compatible with a lot of harm sitting alongside a lot of benefit.
THEO: Alright. What's the takeaway for a practitioner?
MAYA: Three things. First, don't read the average. Look at the distribution. Second, changes in concentration and merging share carry real, if noisy, information. Third, the policy question isn't just whether to be stricter. It's what stricter costs, in agency resources and in deterring proposals.
THEO: And for a researcher, I'd say: the next step is the same design applied outside consumer packaged goods, and some way to bring non-price outcomes into the objective.
MAYA: And better wholesale data. Retail prices are a blurry window onto what the merging firm actually controls.
THEO: Good place to stop.
MAYA [warm]: Thanks for listening. The full citation and a link to the paper are in the show notes, along with what I read and what I didn't.
