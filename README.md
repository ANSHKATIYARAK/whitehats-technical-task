# WhiteHats Recruitment Task - Technical Domain

## 1. Candidate Details
- **Name:** Ansh Katiyar
- **Registration Number:** 25BIT0333
- **Domain Applied For:** Technical Domain (Cybersecurity • Network Security • Web Development)
- **GitHub Repository:** [https://github.com/ANSHKATIYARAK/whitehats-technical-task](https://github.com/ANSHKATIYARAK/whitehats-technical-task)

---

## 2. Why I Want to Join WhiteHats
I want to join **WhiteHats** because it is the premier cybersecurity community to translate my passion for applied cryptography, network security, and software development into hands-on offensive and defensive expertise:

- **Passionate Learning Environment:** Collaborating with like-minded peers who are actively exploring penetration testing, web application security, reverse engineering, and threat analysis.
- **Hands-on Exposure & CTFs:** Actively participating in Capture The Flag (CTF) challenges, hackathons, and security drills to build practical, real-world defensive and offensive problem-solving skills.
- **Bridging Theory with Practice:** Applying my background in mathematical cryptography, formal protocol verification, and network security to real-world infrastructure and application penetration testing.
- **Collaborative Growth & Mentorship:** Learning from experienced seniors and contributing back to the student tech ecosystem through technical workshops, tooling, and research.

---

## 3. Recent Cybersecurity Incident: The CrowdStrike Global Outage (July 2024)

### Overview
On July 19, 2024, a faulty content configuration update deployed to CrowdStrike's **Falcon Sensor** endpoint agent triggered widespread Blue Screen of Death (BSOD) crashes across approximately 8.5 million Microsoft Windows machines worldwide. The incident crippled international airlines, healthcare facilities, financial banking networks, and government operations.

### Technical Root Cause
- **Privileged Execution Environment:** The Falcon Sensor runs as a Windows kernel-mode driver (`CSAgent.sys`) with Ring 0 privileges to monitor low-level OS behaviors.
- **Channel File 291 Update:** CrowdStrike deployed an automated Rapid Response content update via Channel File 291 targeting novel Named Pipe exploitation techniques.
- **Memory Safety Violation:** A logic defect in the sensor's parser engine caused an unhandled out-of-bounds memory read (access violation) when evaluating the content file. Because the crash occurred within kernel space, Windows could not gracefully recover, triggering an immediate BugCheck `PAGE_FAULT_IN_NONPAGED_AREA` (BSOD).

### Key Industry Takeaways
1. **Kernel vs. User-Space Security:** The disaster highlighted the systemic risks of third-party software executing with unrestricted kernel privileges, accelerating industry momentum toward User Mode (Ring 3) endpoint detection architectures.
2. **Canary & Staged Rollouts:** Security software vendors must implement staged deployment rings and automated canary testing for all updates—including definition and configuration payloads.
3. **Formal Verification & Memory Safety:** Emphasizes the need for memory-safe languages and rigorous input sanitization, bounds checking, and formal verification on all parsed input formats.

---

## 4. Hands-on Security & Verification Tools Used in My Research Project
In my research project on **Post-Quantum Cryptography & Vehicular Network Security (SOLARIS-IoV / DAME-IoV)** under Prof. Ankush Chanda, I worked with several advanced cybersecurity validation suites and frameworks:

- **ProVerif 2.05:** Automated formal verification tool used to rigorously prove secrecy, forward secrecy, and mutual authentication theorems under the Dolev-Yao adversarial model.
- **AVISPA (Automated Validation of Internet Security Protocols and Applications) with SPAN:** Multi-oracle automated protocol analysis (OFMC, CL-AtSe, SATMC, TA4SP) verifying immunity against Replay, Man-in-the-Middle (MITM), and Impersonation attacks.
- **NIST SP 800-22 Cryptographic Randomness Suite:** Evaluated 15 statistical randomness battery tests to verify entropy ($p > 0.01$, Shannon entropy = 3.3216 b/sym) in cryptographic primitives.
- **Albrecht Lattice Security Estimator (`lattice-estimator`):** Assessed concrete classical ($2^{124.1}$) and quantum ($2^{109.2}$) bit-security margins against lattice reduction algorithms (BKZ 2.0).
- **Custom Adversarial Attack Simulator (Python):** Developed test suites simulating Replay attacks (temporal freshness check), MITM payload tampering (nonce/parameter mutation), lattice signature forgery, and cloned OBU hardware spoofing.
- **NS-3 & Eclipse SUMO:** Co-simulated C-V2X PC5 direct sidelink communications, propagation delays, packet loss, and emergency braking kinematics under adversarial network conditions.
