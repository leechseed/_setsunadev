- [HDD Installation and Validation Standard Operating Procedure](#hdd-installation-and-validation-standard-operating-procedure)
    - [1. Physical Inspection](#1-physical-inspection)
    - [2. Connection and Detection](#2-connection-and-detection)
    - [3. SMART Check (Self-Monitoring, Analysis, and Reporting Technology)](#3-smart-check-self-monitoring-analysis-and-reporting-technology)
    - [4. Surface Test for Bad Sectors](#4-surface-test-for-bad-sectors)
    - [5. Partition and Format the HDD](#5-partition-and-format-the-hdd)
    - [6. Performance Benchmarking](#6-performance-benchmarking)
    - [7. Backup Integration](#7-backup-integration)
    - [8. Monitor HDD Health](#8-monitor-hdd-health)


# HDD Installation and Validation Standard Operating Procedure

### 1. Physical Inspection
- **Step 1**: Unbox the HDD carefully and inspect for any physical damage (scratches, dents, etc.).
- **Step 2**: Check the connectors (SATA or power connector) for bends or damage.
- **Step 3**: Ensure all necessary accessories (screws, brackets) are available.

### 2. Connection and Detection
**For Internal HDDs**:
- **Step 1**: Shut down the computer and disconnect it from power.
- **Step 2**: Open the case and locate an available SATA port on the motherboard.
- **Step 3**: Connect the SATA cable from the motherboard to the HDD.
- **Step 4**: Connect the power cable from the PSU (Power Supply Unit) to the HDD.
- **Step 5**: Mount the HDD in the drive bay using screws or brackets.
- **Step 6**: Close the case, reconnect the power, and turn on the system.

**For External HDDs**:
- **Step 1**: Plug the HDD into a USB port using the provided cable.
- **Step 2**: Ensure the drive is powered (some external HDDs have a separate power adapter).

**BIOS/UEFI Detection**:
- **Step 1**: Enter the BIOS/UEFI by pressing the correct key during startup (usually F2, Del, or Esc).
- **Step 2**: Navigate to the "Storage" or "Drives" section and check if the new HDD is detected.
- **Step 3**: If detected, save and exit the BIOS. If not, check the connections and repeat the steps.

### 3. SMART Check (Self-Monitoring, Analysis, and Reporting Technology)
**Windows**:
- **Step 1**: Download and install [CrystalDiskInfo](https://crystalmark.info/en/software/crystaldiskinfo/).
- **Step 2**: Open `CrystalDiskInfo`, and it will automatically display the SMART data for all connected drives.
- **Step 3**: Review the health status (should be "Good") and check attributes like "Reallocated Sector Count", "Power-On Hours", and "Temperature".

### 4. Surface Test for Bad Sectors
**Option 1: Using HD Tune**:
- **Step 1**: Download [HD Tune](https://www.hdtune.com/) (free version).
- **Step 2**: Open `HD Tune`, go to the "Error Scan" tab, and click "Start" to begin scanning for bad sectors.
- **Step 3**: Wait for the scan to complete and verify that no bad sectors were found.

**Option 2: Using chkdsk Command**:
- **Step 1**: Open Command Prompt as Administrator.
- **Step 2**: Type the following command to perform a disk check and fix bad sectors:  
  ```bash
  chkdsk /r X:
  ```
  Replace `X:` with your HDD’s drive letter (e.g., `D:`).
- **Step 3**: Let the scan run and review the results for any errors.

### 5. Partition and Format the HDD
- **Step 1**: Right-click on the Start button and choose “Disk Management”.
- **Step 2**: In Disk Management, find the new HDD (it will appear as unallocated space).
- **Step 3**: Right-click the unallocated space and choose “New Simple Volume”.
- **Step 4**: Follow the wizard:
  - Assign a drive letter.
  - Select a file system: **NTFS** (for Windows) or **exFAT** (for cross-platform usage).
- **Step 5**: Click “Finish” to complete the partition and format process.

### 6. Performance Benchmarking
- **Step 1**: Download [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/).
- **Step 2**: Install and open CrystalDiskMark.
- **Step 3**: Select the new HDD from the dropdown menu.
- **Step 4**: Click "All" to start testing both read and write speeds.
- **Step 5**: Once complete, compare the results with the manufacturer's specifications.

### 7. Backup Integration
- **Step 1**: If the HDD is meant for backup, configure your backup software to use the new drive.
- **Step 2**: In Windows, open Control Panel > System and Security > Backup and Restore to set up the new HDD for backups.
- **Step 3**: Schedule regular backups and ensure that the HDD is listed as your backup destination.

### 8. Monitor HDD Health
- **Step 1**: Use **CrystalDiskInfo** or other monitoring software to regularly check your HDD’s SMART status.
- **Step 2**: Set up alerts for any health changes, such as rising temperatures or reallocated sectors.
- **Step 3**: Periodically run the surface test and SMART checks to catch early signs of wear or failure.

Following these steps ensures that your new HDD is fully validated, properly onboarded, and integrated into your system for long-term use.