from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def export_report_to_pdf(report: dict, output_path: str):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    y = height - 40

    def draw_line(text):
        nonlocal y
        if y < 40:
            c.showPage()
            y = height - 40
        c.drawString(40, y, text)
        y -= 14

    draw_line("Contract Risk Assessment Report")
    draw_line("-" * 50)

    meta = report["contract_metadata"]
    draw_line(f"Contract Type: {meta['contract_type']}")
    draw_line(f"Overall Risk Level: {meta['overall_risk_level']}")
    draw_line(f"Risk Score: {meta['overall_risk_score']}")

    draw_line("")
    draw_line("High Risk Clauses:")
    for clause in report["high_risk_clauses"]:
        draw_line(f"{clause['clause_id']} - {clause['risk_level']}")

    draw_line("")
    draw_line("Summary:")
    draw_line(report["summary"])

    c.save()