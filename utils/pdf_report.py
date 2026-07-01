from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    Spacer,
    SimpleDocTemplate,
    Table,
    TableStyle
)


def create_pdf_report(
    filename,
    video,
    summary,
    sentiment,
    keywords,
    topic,
    question="",
    answer=""
):

    doc = SimpleDocTemplate(
        filename,
        rightMargin=35,
        leftMargin=35,
        topMargin=35,
        bottomMargin=35
    )

    styles = getSampleStyleSheet()

    title = styles["Title"]
    title.alignment = TA_CENTER
    title.textColor = colors.HexColor("#1E3A8A")

    heading = styles["Heading2"]
    heading.textColor = colors.HexColor("#1565C0")

    normal = styles["BodyText"]

    elements = []

    # ---------------------------------------------------
    # Title
    # ---------------------------------------------------

    elements.append(
        Paragraph(
            "YouTube Video Analysis Report",
            title
        )
    )

    elements.append(
        Paragraph(
            datetime.now().strftime(
                "Generated on %d %B %Y at %I:%M %p"
            ),
            normal
        )
    )

    elements.append(Spacer(1, 20))

    # ---------------------------------------------------
    # Video Details Table
    # ---------------------------------------------------

    elements.append(
        Paragraph(
            "Video Information",
            heading
        )
    )

    table_data = [

        ["Title", video["title"]],

        ["Channel", video["channel"]],

        ["Views", video["views"]],

        ["Likes", video["likes"]],

        ["Comments", video["comments"]],

        ["Duration", video["duration"]],

        ["Upload Date", video["upload_date"]]

    ]

    table = Table(
        table_data,
        colWidths=[120, 330]
    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (0,-1), colors.HexColor("#E3F2FD")),

            ("GRID", (0,0), (-1,-1), 0.5, colors.grey),

            ("BOX", (0,0), (-1,-1), 1, colors.black),

            ("BOTTOMPADDING", (0,0), (-1,-1), 8),

            ("TOPPADDING", (0,0), (-1,-1), 8),

            ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),

            ("VALIGN", (0,0), (-1,-1), "TOP")

        ])

    )

    elements.append(table)

    elements.append(Spacer(1,20))

    # ---------------------------------------------------
    # Summary
    # ---------------------------------------------------

    elements.append(
        Paragraph(
            "AI Summary",
            heading
        )
    )

    elements.append(
        Paragraph(summary, normal)
    )

    elements.append(Spacer(1,18))

    # ---------------------------------------------------
    # Sentiment
    # ---------------------------------------------------

    elements.append(
        Paragraph(
            "Sentiment Analysis",
            heading
        )
    )

    elements.append(
        Paragraph(
            f"<b>Sentiment:</b> {sentiment['sentiment']}",
            normal
        )
    )

    elements.append(
        Paragraph(
            f"<b>Confidence:</b> {sentiment['confidence']}",
            normal
        )
    )

    elements.append(
        Paragraph(
            sentiment["reason"],
            normal
        )
    )

    elements.append(Spacer(1,18))

    # ---------------------------------------------------
    # Keywords
    # ---------------------------------------------------

    elements.append(
        Paragraph(
            "Keywords",
            heading
        )
    )

    elements.append(
        Paragraph(
            ", ".join(keywords),
            normal
        )
    )

    elements.append(Spacer(1,18))

    # ---------------------------------------------------
    # Topic
    # ---------------------------------------------------

    elements.append(
        Paragraph(
            "Detected Topic",
            heading
        )
    )

    elements.append(
        Paragraph(
            topic,
            normal
        )
    )

    elements.append(Spacer(1,18))

    # ---------------------------------------------------
    # Question Answer
    # ---------------------------------------------------

    if question:

        elements.append(
            Paragraph(
                "User Question",
                heading
            )
        )

        elements.append(
            Paragraph(
                question,
                normal
            )
        )

        elements.append(Spacer(1,8))

        elements.append(
            Paragraph(
                "AI Answer",
                heading
            )
        )

        elements.append(
            Paragraph(
                answer,
                normal
            )
        )

        elements.append(Spacer(1,18))

    # ---------------------------------------------------
    # Footer
    # ---------------------------------------------------

    elements.append(Spacer(1,20))

    footer = Paragraph(

        "<font color='gray'><b>Generated by YouTube Video Analysis System</b></font>",

        title

    )

    elements.append(footer)

    doc.build(elements)