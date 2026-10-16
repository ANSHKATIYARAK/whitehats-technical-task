# WhiteHats Recruitment Task - Technical Domain

## 1. Candidate Details
- **Name:** Ansh Katiyar
- **Registration Number:** 25BIT0333
- **Domain Applied For:** Technical Domain (Cybersecurity • Network Security • Web Development)
- **GitHub Repository:** [https://github.com/ANSHKATIYARAK/whitehats-technical-task](https://github.com/ANSHKATIYARAK/whitehats-technical-task)

---

## 2. Why I Want to Join WhiteHats
I want to join **WhiteHats** because it is the premier cybersecurity community to translate my passion for applied cryptography, network security, and software development into hands-on offensive and defensive expertise:

- **Bridging Applied Research with Practical Security:** In my research on **Post-Quantum Cryptography & Vehicular Network Security (SOLARIS-IoV / DAME-IoV)** under Prof. Ankush Chanda, I gained extensive experience with formal security protocol verification (**ProVerif 2.05**, **AVISPA/SPAN**), cryptographic randomness testing (**NIST SP 800-22**), lattice security estimation (**Albrecht Estimator**), and simulating adversarial attacks (Replay, MITM, Impersonation). Joining WhiteHats gives me the ideal community to bridge this mathematical and protocol-level foundation with hands-on web application penetration testing, network sniffing, and real-world system defense.
- **Hands-on Exposure & CTFs:** Actively participating in Capture The Flag (CTF) challenges, hackathons, and security drills to build practical, real-world offensive and defensive problem-solving skills alongside motivated peers.
- **Passionate Learning Environment & Tooling:** Collaborating with like-minded members who are exploring penetration testing, reverse engineering, web security, and vulnerability research, while contributing to internal tools and security projects.
- **Collaborative Growth & Mentorship:** Learning from experienced seniors, exchanging technical insights with fellow security enthusiasts, and contributing back to the student tech ecosystem through technical workshops and open-source initiatives.

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
