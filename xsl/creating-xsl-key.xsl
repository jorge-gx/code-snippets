
<?xml version="1.0" encoding="UTF-8"?>
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!--	
    this creates our key
    it gives us all xml_node_name nodes with a particular xml_tag_name	
  -->
  <xsl:key name="xsl-key-name" match="xml_node_name" use="xml_tag_name" />
  <xsl:template match="/Start">
    <!--	
      blah blah blah...
    -->
  </xsl:template>
</xsl:stylesheet>


