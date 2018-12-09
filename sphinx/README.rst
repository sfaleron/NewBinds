
Extract API documentation for manual reuse. Not intended to look pretty or polished.

pip install sphinxcontrib-restbuilder

sphinx-build -b rst <source> <output>

For creating rst sphinx output. Will install sphinx as a dependency if it isn't among the packages managed by pip for that python interpreter. Distibution sphinx (unless pip is updated) or pip-package sphinx under another interpreter likely won't be acknowledged.

If <output> is under <source>, sphinx/restbuilder will recurse into it, and nest the the new output under the old output, if an old one exists. A warning is issued, so it's easy to spot this when this happens. Works okay if the old output is pruned or renamed, but that is a hairy problem to nondestructively automate. Avoid. Possibly, the "exclude_patterns" setting in conf.py could be set in a manner that corrects this issue, but I have not tested this.

A suggested viewer:

pip install restview

There's a check for "DNS rebinding" to avoid a security vulnerability that blows up with no-dns-ip-addresses, so I commented it out. Checking (optonally?) for subnet membership before applying the test might be a good ultimate fix.

The source file where the check occurs: site-packages/restview/restviewhttp.py
