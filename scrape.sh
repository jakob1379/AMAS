#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

wget2 -mpEk \
      --wait 2 \
      --random-wait \
      --level=inf \
      --domains=www.nbi.dk \
      --no-parent \
      https://www.nbi.dk/~koskinen/Teaching/AdvancedMethodsInAppliedStatistics2017/StudentPresentations2017.html
