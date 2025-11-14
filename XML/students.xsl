<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- Match the root element <class> -->
    <xsl:template match="/class">
        <html>
            <body>
                <h2>My Student Collection</h2>

                <table border="3" cellpadding="6">
                    <tr bgcolor="blue" style="color:white;">
                        <th>Name</th>
                        <th>Age</th>
                        <th>Sex</th>
                        <th>Major</th>
                    </tr>

                    <!-- Loop through student nodes inside <class> -->
                    <xsl:for-each select="student">
                        <tr>
                            <td><xsl:value-of select="name"/></td>
                            <td><xsl:value-of select="age"/></td>
                            <td><xsl:value-of select="sex"/></td>
                            <td><xsl:value-of select="major"/></td>
                        </tr>
                    </xsl:for-each>

                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
