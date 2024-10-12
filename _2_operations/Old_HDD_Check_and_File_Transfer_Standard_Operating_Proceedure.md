# Old HDD Check and File Transfer Standard Operating Procedure

## 1. Physically Connecting the HDD

### Option A: Internal Connection
1. **Power off the system** and unplug it.
2. **Open the case** by removing the screws or sliding off the side panel.
3. **Connect the HDD**:
   - **SATA cable**: Connect one end of the SATA cable to the HDD and the other end to an available SATA port on the motherboard.
   - **Power cable**: Connect the SATA power cable from the PSU (Power Supply Unit) to the HDD.
4. **Close the case** and plug the system back in.
5. **Power on the system**. The drive should be recognized automatically if connected properly.

### Option B: External Connection
1. **Use a SATA-to-USB Adapter or External Enclosure**.
2. **Connect the HDD**:
   - Connect the SATA data and power connectors from the adapter/enclosure to the HDD.
3. **Plug the adapter/enclosure into a USB port** on your computer.
4. **Turn on the adapter/enclosure** if it has a power switch.
5. **Boot the system**. The drive should be recognized as an external USB drive.

## 2. Checking the HDD’s Health

1. **Install CrystalDiskInfo**: 
   - Download **CrystalDiskInfo** from its official website and install it.
2. **Run the software**:
   - Check the **SMART status** of your HDD. Look for issues like **Reallocated Sector Count** or other warnings.
   - If warnings are displayed, consider transferring the data as soon as possible.

## 3. Accessing the HDD

1. **Open File Explorer**:
   - The drive should appear as a new drive letter (e.g., D:, E:).
2. **If the drive is not visible**:
   - Right-click on **Start** and select **Disk Management**.
   - If the drive is detected without a drive letter, right-click on the partition and select **Assign Drive Letter**.
   - If the drive is uninitialized, right-click the drive and select **Initialize Disk** (be careful not to format the drive).

## 4. Transferring Files

### Manual Transfer
1. Open **File Explorer** and navigate to the old HDD.
2. Locate the files you want to transfer.
3. **Copy the files** (`Ctrl+C`) and **paste them** (`Ctrl+V`) into the desired folder on your new system.

### Using Command Prompt for Large Transfers
1. Open **Command Prompt**.
2. Use the **Robocopy** command:
   ```bash
   robocopy "D:\OldFolder" "C:\NewFolder" /E /Z /COPYALL
   ```
   - `/E`: Copies all subdirectories, including empty ones.
   - `/Z`: Enables restartable mode for large transfers.
   - `/COPYALL`: Copies all file attributes and timestamps.

## 5. Backup Important Data (Optional)

1. **Cloud Backup**: Upload important files to cloud services like Google Drive or OneDrive.
2. **External HDD/SSD Backup**: Copy files to an external hard drive or SSD using the same manual or command prompt method as above.

## 6. Safely Disconnect the HDD

1. For external drives, **eject the drive**:
   - Right-click on the USB icon in the taskbar and select **Eject**.
2. For internal drives, **power off the system**:
   - Open the case and disconnect the SATA and power cables from the HDD. Close the case and power the system back on.