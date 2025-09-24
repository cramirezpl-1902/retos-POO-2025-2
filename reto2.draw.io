<mxfile host="app.diagrams.net">
  <diagram id="UMLBiblioteca" name="Sistema Biblioteca">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Usuario -->
        <mxCell id="2" value="Usuario\n- idUsuario\n- nombre\n- email\n\n+ registrarse()\n+ consultarPrestamos()" style="shape=rectangle;rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="40" width="180" height="120" as="geometry"/>
        </mxCell>

        <!-- Estudiante -->
        <mxCell id="3" value="Estudiante\n- carrera\n- semestre" style="shape=rectangle;rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="20" y="200" width="160" height="80" as="geometry"/>
        </mxCell>

        <!-- Profesor -->
        <mxCell id="4" value="Profesor\n- departamento" style="shape=rectangle;rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="230" y="200" width="160" height="80" as="geometry"/>
        </mxCell>

        <!-- Herencia -->
        <mxCell id="5" edge="1" parent="1" source="3" target="2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="6" edge="1" parent="1" source="4" target="2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Libro -->
        <mxCell id="7" value="Libro\n- isbn\n- titulo\n- autor\n- estado\n\n+ cambiarEstado()\n+ mostrarInfo()" style="shape=rectangle;rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="480" y="40" width="200" height="120" as="geometry"/>
        </mxCell>

        <!-- Prestamo -->
        <mxCell id="8" value="Prestamo\n- idPrestamo\n- fechaInicio\n- fechaFin\n- estado\n\n+ registrar()\n+ finalizar()" style="shape=rectangle;rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="480" y="220" width="200" height="120" as="geometry"/>
        </mxCell>

        <!-- Asociación Libro-Prestamo -->
        <mxCell id="9" edge="1" parent="1" source="8" target="7">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Bibliotecario -->
        <mxCell id="10" value="Bibliotecario\n- idEmpleado\n- nombre\n\n+ registrarLibro()\n+ gestionarPrestamo()\n+ gestionarDevolucion()" style="shape=rectangle;rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="750" y="120" width="220" height="120" as="geometry"/>
        </mxCell>

        <!-- Relación Prestamo-Bibliotecario -->
        <mxCell id="11" edge="1" parent="1" source="10" target="8">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
