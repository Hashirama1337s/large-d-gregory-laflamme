# Sealed-test records for Paper I: hashes

For each file: the SHA-256 value(s) recorded in the seal file at sealing (a seal file may list a path more than once
when it was re-hashed after a disclosed edit), the SHA-256 of the lab original at assembly time, and the SHA-256 of
the copy in this deposit. "redacted = yes" means the deposited copy differs from the lab original only by the
replacement of lab-machine paths with <lab>/, <home>/ or <private folder>/, of a personal name with [owner], and of
one approximate time written with a trailing x by its explicit minute range. A reader can check a redacted copy
only against its own listed hash,
not against the seal.

| test | file | seal file | sealed sha256 | original now matches a sealed value | deposited copy sha256 | redacted |
|---|---|---|---|---|---|---|
| K5 | BAR-K5.md | SEAL-K5.sha256 | 8ee216d2e92f9346... | yes | bff3e28c71ea6e887e298324d093aac688122a04f100ee9887380ed34f0ee844 | yes |
| K5 | verdict_k5.py | SEAL-K5.sha256 | bb143c91176468e0... | yes | 63583145633cdd010a464f34e881291e37d23822344d6521ad24b576d3d59cb2 | yes |
| K5 | verdict-K5.txt | SEAL-K5.sha256 | 58744b58859e626f... | yes | 58744b58859e626f90d532768c7e9f22a96e15b199fdb007cbc9885e6bac493e | no |
| K8 | BAR-K8.md | SEAL-K8.sha256 | 12089bfbf0135cac... | yes | 12089bfbf0135cac3033dccef01d01361a1979b4a035bcea8322052e0e543ec7 | no |
| K8 | verdict_k8.py | SEAL-K8.sha256 | c991d11703954a4f... | yes | 8204105ef4b92866898de423199b7773e5d265c2b773c547b6449bfc321547e3 | yes |
| K8 | verdict-K8.txt | SEAL-K8.sha256 | 7c146ae7e3ef2a5c... | yes | 7c146ae7e3ef2a5c6d46d1330672001f0aea46285eb45827d7ea2efd2b8fa724 | no |
| DERIV | BAR-DERIV.md | SEAL-ROUND3.sha256 | e4d566da09e021cd... | yes | 880adf040ad4ac74ab97f05b65aff8533365135d0ad128ce5de884a5de321703 | yes |
| DERIV | verdict_deriv.py | SEAL-ROUND3.sha256 | 898824a925638013... | yes | 07951ba71cb70f454aae7f767b6f6679e8a64b1c710898e9345e1a5aff1e66dc | yes |
| DERIV | verdict-DERIV.txt | SEAL-ROUND3.sha256 | 4a0ad0242a245855... | yes | 4a0ad0242a2458559c47cb33ed9eeabd8507fda56a807a4d9317143b1d6ab39f | no |
| K11 | BAR-K11.md | SEAL-K11.sha256 | f3244ea1292d69da... | yes | f3244ea1292d69dae19f70a0ed6a324f687f479d15a44e55a8fd7770626c32b5 | no |
| K11 | verdict_k11.py | SEAL-K11.sha256 | a5f014c915f97173... | yes | b41aa0a8db9df7e9535d209cb79e48c9f3a1aaa30ea951bdfaefccf427e13b61 | yes |
| K11 | verdict-K11.txt | SEAL-K11.sha256 | eb53b5927ec944ec... | yes | eb53b5927ec944ec788f2bea05e7d39bac99c96d87729a9dee6587f2d1d86f31 | no |
| R2 | BAR-R2.md | SEAL-R12.sha256 | 7a4278c6e137d758... | yes | 91b831dcf2236d8ba72ce903efd0aa8fa3e55fd35a673a65c643e976923f4ed0 | yes |
| R2 | verdict_r2.py | SEAL-R12.sha256 | 680a60a5659d89e0... | yes | 8b5278d3ae26d10cb5224c534f18409089588e3f0f35060d98e382e0ed6f6bfe | yes |
| R2 | verdict-R2.txt | SEAL-R12.sha256 | 5849e8f56942d50e... | yes | 5849e8f56942d50ef01d72a0560df6b0058f215fb7eb3223b2fafb183725fd76 | no |
| R1 | BAR-R1.md | SEAL-R12.sha256 | 483e697da05e95cb... | yes | 483e697da05e95cbe784ed2c7e3ce92b3a3787d4b58222f9322caf4dd3fb69e8 | no |
| R1 | verdict_r1.py | SEAL-R12.sha256 | 99311297521e8632... | yes | fd6cef09febbf400d4e122598a5a9f808fe1f94af9e1799a95fecc4ad5b3f96c | yes |
| R1 | verdict_r1_numeric.py | SEAL-R12.sha256 | c39ae3695260063c... / c39ae3695260063c... | yes | 39f49cbeac20a3672bf4421f7dd74985557cfb9cc830d98a54470b1b8a845630 | yes |
| R1 | verdict-R1.txt | SEAL-R12.sha256 | 68a584d007c36a59... / 68a584d007c36a59... | yes | 68a584d007c36a592a07afc016177a35c2dea2273de23930eac967c94b806254 | no |
| NP | BAR-NP.md | SEAL-NP.sha256 | d546ff97dc29a2f5... | yes | d546ff97dc29a2f58856052477ab9460fcd4b48f4136d6666be9f0303e883316 | no |
| NP | verdict_np.py | SEAL-NP.sha256 | 18d0eecb54ed9638... | yes | 745bf7c8029b26204824b5543ce0e3c6e7b86673e498d8aedf19c850ad2f0424 | yes |
| NP | verdict-NP.txt | SEAL-NP.sha256 | 234461a0993ead4f... | yes | 234461a0993ead4fe74b8ec92b01eb98ba43bc7b7aba8c85faf3c7c22bb19710 | no |
| ADS | BAR-ADS.md | SEAL-ADS.sha256 | 101b70b2515c1a3e... | yes | 8895f968d895e5c844cc44add23a8a8d9f485d744a9d6ff3abeb303f1040ef30 | yes |
| ADS | verdict_ads.py | SEAL-ADS.sha256 | 21186bcb09c4e24f... | yes | c8e21338c8ee05bccb8ad6571e6e0db47e1ddb89fdce659ae072413e286e9057 | yes |
| ADS | verdict-ADS.txt | SEAL-ADS.sha256 | 2bc5255847cbd1d0... | yes | 2bc5255847cbd1d06cf740f3fbd9a594648842a0c1627c1abc1487965be1f2bf | no |
| F1 | BAR-F1.md | SEAL-F1.sha256 | c3fda09de87619e5... | yes | c3fda09de87619e53e96e78750146108fea03d0655f5f025c24af9d0ec56f8ec | no |
| F1 | predict_F1.py | SEAL-F1.sha256 | 541dd7ec63a599c5... | yes | 4711780c802f846e27ede407e1268f3ba0f855650e0968bbe71eccb747a4ce94 | yes |
| F1 | PRED-F1.json | SEAL-F1.sha256 | 2051d56d6a6b3a13... | yes | 2051d56d6a6b3a132d82bf9ec62d2af5bfe6357cbd22e0e3b411f37862049296 | no |
| F1 | verdict_F1.py | SEAL-F1.sha256 | 035d47fccd684daf... | yes | 125c921245b6ab4e64fcbe187c3c3fb2a4b055c375e0c817f4660c5d70b391c1 | yes |
| F1 | verdict-F1.txt | SEAL-F1.sha256 | 03c5bbfddf40db10... | yes | 03c5bbfddf40db10f4c9ff4d1e7ae91cf8f60603d9b3f9f706bff26b429f4dc4 | no |
| F1 | blindAdS/RESULT.json | SEAL-F1.sha256 | 9a39f4ad474b0761... | yes | 9a39f4ad474b0761c4d41916d14d6b809db2bb69260c5d6f81c2655703998b5b | no |
| F2 | BAR-F2.md | SEAL-F2.sha256 | 68d1ef4c250c1953... | yes | 68d1ef4c250c19532514ea9674b15ea5cb857b00aaab939c96f6cb9aa6712b51 | no |
| F2 | predict_F2.py | SEAL-F2.sha256 | 78c816f7eceeb9a8... | yes | 77ad0b78d6869372d3cf45692b2f908158b7f42e6c6df559a6cd7b4719b2f35b | yes |
| F2 | PRED-F2.json | SEAL-F2.sha256 | 0ad8521f9f2e11e0... | yes | 0ad8521f9f2e11e034ca04b145a72463c118db9a051233de0e92d090ce52018f | no |
| F2 | verdict_F2.py | SEAL-F2.sha256 | 6d476050fdbb9f4e... | yes | 4acd0a71488fc0c3f8f87dcde51579fcb6f6ba9c2aff1e001b6218762bfbf20b | yes |
| F2 | verdict-F2.txt | SEAL-F2.sha256 | 191f3fd2e49ca5ac... | yes | 191f3fd2e49ca5ac219c2ddad4a8cdd4c592e99839177fd229f061b76199fc04 | no |
| F2 | DISCLOSURE-F2.md | SEAL-F2.sha256 | 7ed19779a912988f... | yes | ea18b7ae56bf7de8bdd73830219251c853ccc2a3762ed054dadeccbcfa7c79d6 | yes |
| F2 | blind/RESULT.json | SEAL-F2.sha256 | 2e429166a9550a19... | yes | 2e429166a9550a19e744ecd5f0574e62186787b964299feea5bb4e8cc60bad7d | no |
| SB | BAR-SB.md | SEAL-SB.sha256 | a793b63d1a86d994... | yes | a793b63d1a86d99485617edd9f8e4c3baff8aec8a4785b936856c7e4488ba633 | no |
| SB | verdict_SB.py | SEAL-SB.sha256 | def955f9e833a176... | yes | 9130c1b3ba486a83011daaca8f559c83c4022519bb5bdbe2dc0ffea8f3139066 | yes |
| SB | verdict_SB_scored.py | SEAL-SB.sha256 | 70ae0039aa95e856... | yes | 9f067295a5b71eceb4c7ebb613f189d9b71efe7675bae705eb088924a242ef18 | yes |
| SB | verdict-SB.txt | SEAL-SB.sha256 | 9aa509f1005b063f... | yes | 9aa509f1005b063fdfa8fefc7df1a4930047287cacbd10ee894107abbcabfab1 | no |
