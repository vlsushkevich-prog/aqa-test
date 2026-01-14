import xml.etree.ElementTree as ET
from dummy_test_runner import *


root = ET.Element('test_report')

total = ET.SubElement(root, 'total', {'total_tests': f'{str(results['total_tests'])}'})

passed = ET.SubElement(root, 'passed')
passed.set('amount', str(results['passed']['passed_amount']))
passed.set('percentage', f'{results['passed']['passed_percentage']}')

failed = ET.SubElement(root, 'failed')
failed.set('amount', str(results['failed']['failed_amount']))
failed.set('percentage', f'{results['failed']['failed_percentage']}')

error_messages = ET.SubElement(failed, 'error_messages')
for message in results['failed']['errors']:
    error_item = ET.SubElement(error_messages, 'error')
    error_item.text = message

tree = ET.ElementTree(root)
ET.indent(tree, space='\t', level=0)
tree.write('dummy_test_results.xml', encoding='utf-8', xml_declaration=True)

