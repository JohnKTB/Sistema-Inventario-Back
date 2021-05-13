import io

from django.http import FileResponse
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.Facturacion.models import detVenta
from applications.Facturacion.serializers import detVentaListSerializer, detVentaListPDFSerializer


class testeando(ListAPIView):
    serializer_class = detVentaListSerializer
    queryset = detVenta.objects.all().order_by('id')

    def list(self, request, *args, **kwargs):
        """print('*****')
        print(self.kwargs['id_recibo'])
        return Response({})"""

        buffer = io.BytesIO()

        # objeto de lienzo que generara un archivo pdf
        p = canvas.Canvas(buffer)
        # Este es el color de los bordes
        p.setStrokeColorRGB(0.2, 0.5, 0.3)
        p.setFillColorRGB(1, 0, 1)
        p.rect(0, 700, 600, 20, fill=1)
        p.setFillColorRGB(0, 0, 0.77)
        p.setFont("Helvetica-Bold", 9)
        p.drawString(50, 705, 'Cantidad')
        p.drawString(150, 705, 'Descripcion')
        p.drawString(300, 705, 'Precio Unit.')
        p.drawString(400, 705, 'Precio Total')
        p.drawString(500, 100, self.kwargs['id_recibo'])
        """El método showPage hace que el lienzo deje de dibujar en la página
         actual y cualquier otra operación. se dibujará en una página posterior
          (si hay más operaciones, si no, no se crea una nueva página)"""
        p.showPage()
        p.save()

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


class PDF(APIView):

    def post(self, request, format=None):
        detVentQuery = detVenta.objects.filter(venta=request.data['venta']['id'])
        serializer = detVentaListPDFSerializer(detVentQuery, many=True).data
        print('*******')
        print(serializer)
        print(serializer[0]['venta']['precioT'])
        buffer = io.BytesIO()

        # objeto de lienzo que generara un archivo pdf
        p = canvas.Canvas(buffer)
        # Este es el color de los bordes
        p.setStrokeColorRGB(0.2, 0.5, 0.3)
        p.setFillColorRGB(1, 0, 1)
        p.rect(0, 700, 600, 20, fill=1)
        p.setFillColorRGB(0, 0, 0.77)
        p.setFont("Helvetica", 11)
        p.drawString(50, 705, 'Cantidad')
        p.drawString(150, 705, 'Descripcion')
        p.drawString(300, 705, 'Precio Unit.')
        p.drawString(400, 705, 'Precio Total')
        posicionVertCamp = 680
        posicionVertRec = 670
        dx = 0.4 * inch

        p.setFont("Helvetica", 8)
        for index, campo in enumerate(serializer):
            p.setFillColorRGB(0.3, 0.9, 0.2)
            p.rect(0, posicionVertRec, 600, 20, fill=1)
            p.setFillColorRGB(0, 0, 0.77)
            p.drawString(55, posicionVertCamp, str(serializer[index]['cantidad']))
            p.drawString(155, posicionVertCamp, str(serializer[index]['producto']['nombre']))
            p.drawString(305, posicionVertCamp, str(serializer[index]['precioU']))
            p.drawString(405, posicionVertCamp, str(serializer[index]['precioT']))
            posicionVertCamp -= dx
            posicionVertRec -= dx
        """El método showPage hace que el lienzo deje de dibujar en la página
         actual y cualquier otra operación. se dibujará en una página posterior
          (si hay más operaciones, si no, no se crea una nueva página)"""
        p.showPage()
        p.save()

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
