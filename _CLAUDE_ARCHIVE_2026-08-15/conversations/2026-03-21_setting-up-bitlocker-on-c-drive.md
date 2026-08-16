---
title: "Setting up BitLocker on C: drive"
uuid: ea06e851-eb53-459f-a514-99c898ea9cb7
created: 2026-03-21
updated: 2026-03-21
trunk: BLACK
messages: 2
chars: 2366
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Setting up BitLocker on C: drive

> **Conversation Overview**

The person asked for help setting up BitLocker encryption on their C: drive. Claude provided a comprehensive step-by-step walkthrough covering prerequisites (Windows edition requirements, TPM chip), the full setup process through the BitLocker management interface, recovery key backup options (Microsoft account, USB, file, or print), encryption scope choices (used space vs. full drive), and encryption mode selection (XTS-AES recommended for fixed drives). Claude also covered important caveats including avoiding powering off during encryption, the significance of preserving the recovery key, and how to retrieve it via the Microsoft account recovery key portal. Additionally, Claude proactively explained the workaround for systems without a TPM chip, which involves modifying a Group Policy setting to allow BitLocker with a USB startup key or password instead. The conversation was casual in tone, with the person using informal language. Claude closed by offering further help with the no-TPM workaround or command-line BitLocker management.

---
## 🧑 Papi  <sub>2026-03-21 04:59:55</sub>

bro help me set up bitlocker on my C: drive please

---

## 🤖 Claude  <sub>2026-03-21 05:00:15</sub>

The user is asking about setting up BitLocker on their C: drive. This is a Windows feature - I can answer this from knowledge, no tools needed.Hey! Happy to walk you through setting up BitLocker on your C: drive. Here's what you need to know:

**Before you start**, make sure your system supports it. BitLocker is available on Windows 10/11 Pro, Enterprise, and Education editions — it's not on Home edition. Your PC also needs a TPM (Trusted Platform Module) chip, which most modern machines have.

**To turn it on:**

1. Open **Settings → Privacy & security → Device encryption** (on Windows 11) or search "BitLocker" in the Start menu and open **Manage BitLocker**.
2. Next to your **C: drive**, click **Turn on BitLocker**.
3. Windows will ask how you want to back up your recovery key. You'll get options like saving it to your Microsoft account, a USB drive, a file, or printing it. **Pick at least one and keep it safe** — if you lose this key and get locked out, your data is gone.
4. Choose whether to encrypt **used disk space only** (faster, good for new/clean installs) or the **entire drive** (more secure, better for drives already in use).
5. Select the encryption mode — **New encryption mode (XTS-AES)** is best for fixed drives like your C: drive.
6. Check the box to run the BitLocker system check (recommended), then click **Start encrypting**.
7. Your PC will restart, and encryption will begin in the background. You can keep using your machine while it works.

**A few things to keep in mind:**

- Encryption can take a while on large drives — don't power off mid-process.
- If your PC doesn't have a TPM, you can still use BitLocker with a USB startup key or password, but you'll need to tweak a Group Policy setting first (`gpedit.msc → Computer Configuration → Administrative Templates → Windows Components → BitLocker Drive Encryption → Operating System Drives → Require additional authentication at startup`).
- **Back up that recovery key seriously.** Microsoft account is the most convenient option since you can retrieve it from any browser at `account.microsoft.com/devices/recoverykey`.

Want help with anything specific, like the no-TPM workaround or managing BitLocker via command line?