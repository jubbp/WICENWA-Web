// pdftool.swift — small PDFKit helper for the manual build.
//   swift pdftool.swift pages <file.pdf>
//   swift pdftool.swift render <file.pdf> <outdir> <dpi>     -> page-001.jpg …
//   swift pdftool.swift find <file.pdf> <marker-prefix>      -> "<marker> <page>" per match
import Foundation
import PDFKit
import AppKit

let args = CommandLine.arguments
guard args.count >= 3, let doc = PDFDocument(url: URL(fileURLWithPath: args[2])) else {
    FileHandle.standardError.write("cannot open PDF\n".data(using: .utf8)!); exit(1)
}

switch args[1] {
case "pages":
    print(doc.pageCount)
case "render":
    let out = URL(fileURLWithPath: args[3]); let dpi = CGFloat(Double(args[4]) ?? 150)
    try? FileManager.default.createDirectory(at: out, withIntermediateDirectories: true)
    for i in 0..<doc.pageCount {
        guard let page = doc.page(at: i) else { continue }
        let box = page.bounds(for: .mediaBox)
        let scale = dpi / 72
        let w = Int(box.width * scale), h = Int(box.height * scale)
        let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h, bitsPerSample: 8,
                                   samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                                   colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
        NSGraphicsContext.saveGraphicsState()
        let ctx = NSGraphicsContext(bitmapImageRep: rep)!
        NSGraphicsContext.current = ctx
        ctx.cgContext.setFillColor(NSColor.white.cgColor)
        ctx.cgContext.fill(CGRect(x: 0, y: 0, width: w, height: h))
        ctx.cgContext.scaleBy(x: scale, y: scale)
        page.draw(with: .mediaBox, to: ctx.cgContext)
        NSGraphicsContext.restoreGraphicsState()
        let data = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.7])!
        try! data.write(to: out.appendingPathComponent(String(format: "page-%03d.jpg", i + 1)))
    }
    print(doc.pageCount)
case "find":
    let prefix = args[3]
    for i in 0..<doc.pageCount {
        guard let text = doc.page(at: i)?.string else { continue }
        var rest = Substring(text)
        while let r = rest.range(of: prefix) {
            let tail = rest[r.lowerBound...].prefix { !$0.isWhitespace }
            print("\(tail) \(i + 1)")
            rest = rest[r.upperBound...]
        }
    }
default:
    exit(2)
}
