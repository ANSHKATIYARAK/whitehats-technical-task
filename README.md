# WhiteHats Recruitment Task - Technical Domain

## 1. Candidate Details
- **Name:** Ansh Katiyar
- **Registration Number:** 25BIT0333
- **Domain Applied For:** Technical Domain (Cybersecurity / Web Development / Network Security)

---

## 2. Why I Want to Join WhiteHats
I want to join **WhiteHats** because it is the premier platform to translate my curiosity in cybersecurity and software engineering into hands-on, practical expertise. Here are the core reasons:

- **Passionate Learning Environment:** I want to dive deep into network security, web application penetration testing, and ethical hacking alongside like-minded peers who are actively exploring security domains.
- **Hands-on Exposure & CTFs:** WhiteHats actively engages in Capture The Flag (CTF) competitions, hackathons, and research projects. Participating in these will hone my defensive and offensive security problem-solving skills.
- **Collaborative Growth & Mentorship:** Learning from experienced seniors and collaborating on real-world projects will accelerate my technical growth, while giving me an avenue to contribute back to the student tech community through workshops and open-source tooling.

---

## 3. Recent Cybersecurity Incident: The CrowdStrike Global Outage (July 2024)

### Overview
On July 19, 2024, a faulty content configuration update deployed to CrowdStrike's **Falcon Sensor** agent triggered widespread Blue Screen of Death (BSOD) crashes on approximately 8.5 million Microsoft Windows systems worldwide. It severely disrupted airlines, hospitals, banking institutions, and critical infrastructure globally.

### Technical Cause
- The Falcon Sensor operates as a kernel-level driver (`CSAgent.sys`) on Windows to monitor system activity with deep privileges.
- CrowdStrike pushed an update containing a **Channel File 291** designed to detect novel threat-actor techniques.
- The update introduced a logic error / out-of-bounds memory read within the sensor's parser engine, causing an unhandled memory access violation in the kernel driver. Because the code was running in Kernel Mode (Ring 0), the OS could not gracefully recover, leading to an immediate kernel panic (BSOD `PAGE_FAULT_IN_NONPAGED_AREA`).

### Key Takeaways for the Security Industry
1. **Kernel-Level Risks & Principle of Least Privilege:** Running third-party security software in kernel mode presents a single point of catastrophic failure. The incident accelerated discussions around moving endpoint detection (EDR) sensors to User Mode (Ring 3) through safer abstractions.
2. **Staged Rollouts & Canary Deployments:** Critical updates—even configuration definitions—must be staged progressively (canary testing, validation rings) rather than simultaneous global rollout.
3. **Robust Input Validation & Memory Safety:** Rigorous bounds checking and formal validation of incoming rule files are critical even for internal signed binaries.
