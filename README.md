# Splash Image Maker, a pure Python variant
Creates a splash.img image to modify splash screen on Alcatel Idol 3 4.7 (model 6039).

## Credits
* Gokul NC
* persona78 for modification for Alcatel Idol 3 (4.7 inch version) 
See original post [here](https://forum.xda-developers.com/idol-3/general/guide-how-to-create-custom-boot-logo-t3472663/)
* Original Qualcomm script [here](https://source.codeaurora.org/quic/la/device/qcom/common/tree/display/logo?h=LA.BR.1.2.7_rb1.1)

## Requirements 
* Python 2.7 (for obscure StringIO compatibility reasons)
* Python Image Library PIL (sudo apt install python-pil)

## Usage
Create or modify the image you want to apply to splash screen
but must be 720x1280 size and save it as "logo.png" in pics subfolder.
Also edit or modify the download mode splash screen and save it as "download\_mode.png" in pics folder.

If everything is ok you will get a splash.img file in the current directory.
Copy the image in the splash partition (/dev/block/bootdevice/by-name/splash) with TWRP or QFIL.

