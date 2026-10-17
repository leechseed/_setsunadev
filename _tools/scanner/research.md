# Scanner research: Epson ES-590W intake (BOLO 107)

Written 2026-10-17 from web sources only. "Unverified" marks claims I could not confirm.

## Verdict

- **Use NAPS2 to scan.** It is free, open source, drives the scanner through TWAIN or WIA, and has a command line. [naps2.com](https://www.naps2.com/) · [CLI docs](https://www.naps2.com/doc/command-line)
- **Use OCRmyPDF for text.** It fixes tilt and rotation, and writes a searchable PDF/A plus a text file. [cookbook](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html)
- **Do not trust Tesseract on handwriting.** Use a vision model that reads page images for the story-bible notes. Keep TrOCR as a second option.
- **Keep ScanSmart installed as a fallback only.** Its driver (Epson Scan 2) is what NAPS2 talks to anyway.
- **Scan handwriting at 300 dpi color, saved lossless.** Always keep the raw scan. Never OCR over the only copy.

## ScanSmart: what's wrong

- **Auto file naming can guess wrong.** It reads a date and subject from the image with OCR. Epson lists "Files are Named with an Old Date" as a known problem. The fix is to turn the option off. [Epson help](https://download4.epson.biz/sec_pubs/ScanSmart/r/en/GUID-096E28F8-DD0D-4F11-B2D3-CAD9469EE09E_ie.htm)
- **OCR can fail.** Epson's own guide has a troubleshooting topic, "Characters are Not Recognized During Conversion to Editable Text (OCR)". [User's Guide](https://files.support.epson.com/docid/cpd5/cpd57811/helpcontents.html)
- **Cloud sending breaks.** "Cannot Send Scans to a Cloud Service" is also a listed topic. Same page.
- **It is built for a person at the screen.** One third-party comparison says it suits review-then-save work, and that unattended saving to folders fits panel-based scanning better. This is the writer's inference, not a documented limit. [kitemetric](https://kitemetric.com/blogs/effortless-scanning-master-epson-scansmart)
- **Closed source, no scripting.** I found no hot folder, no command line and no batch API in the docs. Absence of evidence, not proof. Unverified.
- **I found no forum threads of user complaints.** The list above comes from Epson's own docs.

## Alternatives

| Name | Open source? | Drives ES-590W how | OCR | Automation | Cons |
|---|---|---|---|---|---|
| **NAPS2** | Yes | WIA or TWAIN via Epson Scan 2; the CLI also lists an ESCL driver (Wi-Fi) [CLI](https://www.naps2.com/doc/command-line) | Built in, 100+ languages [site](https://www.naps2.com/) | `naps2.console`: profiles, `--source duplex`, `--autosave`, `-o file.pdf` | Blank-page skip is not on the CLI page (unverified). No true hot-folder watch. |
| **Paperless-ngx** | Yes | Not a scan driver. It is the archive that watches a consume folder. | Uses OCRmyPDF inside | Consume folder, tags, dedupe | Needs Docker or a server. Its docs returned 403 to me, so details are unverified. [docs](https://docs.paperless-ngx.com/configuration/) |
| **ScanSmart** | No | Epson's own | Epson OCR | Almost none | See above |
| **VueScan** | No (paid) | Its own drivers | Yes | Some | Not open source. Skip. |

## Settings per material

ES-590W facts: 100-sheet feeder, 600 dpi optical, 215.9 mm wide max. Ultrasonic double-feed detection is stated for the ES-550W family and is likely on the 590W. [datasheet](https://www.thescannershop.com/files-client/docs/workforce-es-590w-datasheet.pdf) · [Epson press](https://press.epson.eu/en_GB/news/epson-launches-es-550w-and-es-590w-wireless-scanners-to-power-fast-flexible-document-digitisation-for-modern-workplaces/)

The settings below are my recommendations, not from a source. OCRmyPDF does say wrong input resolution hurts OCR. [cookbook](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html)

| Material | dpi | Color | Duplex | Blank skip | Double-feed detect | Deskew | File |
|---|---|---|---|---|---|---|---|
| Typed pages / scripts | 300 | Gray | On | On | On | On | PDF, then OCR |
| Handwriting | 300 (400 for tiny pen) | Color | On | Off at first (a faint page is not blank) | On | Off at scan, fix in pipeline | Lossless PNG or TIFF, plus PDF |
| Photos | 600 | Color | Off | n/a | Off, use carrier sheet | Off | TIFF or high-quality JPEG |
| Receipts | 300 | Gray | Off | On | Off, use carrier sheet | On | PDF, JPEG quality about 60 |

ADF limits:
- Epson recommends the optional carrier sheet (part B12B819051) for creased, valuable or thin originals such as receipts. [Epson FAQ](https://epson.com/faq/SPT_B11B288202~faq-00008dd-es590w)
- A third-party seller does not list the ES-590W as compatible with that sheet. Check before buying. [Adorama](https://www.adorama.com/epson-carrier-sheets-ds-80w-ds-70-portable-document-scanners/p/ies12b819451)
- Bound notepads do not feed. Tear out the pages or photograph them. This is my reasoning about a sheet-fed design, not a cited page.
- Max length is 6,096 mm. Min size is 50.8 mm square. [datasheet](https://www.thescannershop.com/files-client/docs/workforce-es-590w-datasheet.pdf)

## The pipeline

1. **Scan** with `naps2.console` using a saved profile. Output goes to `_scan_in/`. Raw files are copied to `_scan_raw/` and never touched again.
2. **Watch the folder** with a small Python script (poll every few seconds, wait until the file size stops changing). I could not confirm any NAPS2 hot folder.
3. **Run OCRmyPDF** on typed material: `ocrmypdf --deskew --rotate-pages --output-type pdfa --optimize 1 --sidecar out.txt -l eng in.pdf out.pdf`. [flags](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html)
4. **Use `--clean`, not `--clean-final`.** The page image stays unchanged. The docs warn `--clean-final` can leave artifacts. Same page.
5. **Handwriting skips Tesseract** and goes to the handwriting step below.
6. **Name** files `YYYY-MM-DD_source_batch_NNN`. Do not use ScanSmart's guessed names.
7. **Dedupe** by SHA-256 of the raw scan, plus a perceptual hash for near-duplicates. My suggestion, not sourced.
8. **File** into Zotero or a folder tree. Paperless-ngx is optional.

## Handwriting

- **Tesseract is weak here.** iText's docs say handwriting recognition is not supported at this stage. [iText KB](https://kb.itextpdf.com/itext/pdfocr-is-handwriting-recognition-supported)
- **TrOCR runs on a 3090 but reads one line at a time.** A multi-line image gave meaningless output in a user report. You need a line-splitting step first. [HF forum](https://discuss.huggingface.co/t/handwriting-recognition-cant-recognize-multiline-words/39422) · [paper](https://arxiv.org/pdf/2602.14524)
- **TrOCR scores well on clean line images.** The IAM benchmark lists TrOCR-large at 2.89 CER. IAM is tidy sample handwriting, not Chief's notepads. [benchmark](https://vercel.hyper.ai/en/sota/tasks/handwritten-text-recognition/benchmark/handwritten-text-recognition-on-iam)
- **A vision model can read whole pages.** The paper notes Qwen's vision model can take full-page images. [paper](https://arxiv.org/pdf/2602.14524) I found no head-to-head accuracy numbers. Unverified.
- **Plan:** run a vision model on each page image, write a draft transcript next to the scan, and mark unclear words `[?]`. Chief spot-checks. Test 20 real pages before trusting it.

## Risks and unknowns

- **ES-590W under NAPS2 is untested.** TWAIN and WIA should work through Epson Scan 2. No source confirms it. Scan one page first.
- **ESCL over Wi-Fi on this model is unverified.** USB with TWAIN is the safe path.
- **NAPS2 blank-page skip and its CLI flag are unverified.** If missing, drop blank pages in the pipeline script.
- **Double-feed detection on the 590W is inferred** from ES-550W press text.
- **Carrier sheet fit for the 590W** has conflicting evidence.
- **Tesseract has only eng and osd.** Add languages if needed.
- **Vision-model handwriting accuracy is untested.** Cloud models would send private notes off the box. Prefer a local model.
- **Fix for each weak spot:** keep raw scans, keep the sidecar text, log every step, and keep ScanSmart as a fallback.
