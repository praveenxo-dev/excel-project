import excel2img


def export_excel_to_image(excel_file, output_image, sheet_name, cell_range):
    excel2img.export_img(
        excel_file,  # Excel file
        output_image,  # Output image
        sheet_name,
        cell_range,  # Range to capture
    )
