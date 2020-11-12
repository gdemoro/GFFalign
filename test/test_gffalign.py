#!/usr/bin/env python3

from subprocess import Popen, PIPE



def test_entrypoint():
    test_status = Popen(["gffalign", "--help"], stdout=PIPE)
    (output, err) = test_status.communicate()
    exit_code = test_status.wait()
    assert exit_code == 0


def test_output():
    test_status = Popen(["gffalign", "-m", "genome_aln.tab", "query.gff", "target.gff"], stdout=PIPE)
    (output, err) = test_status.communicate()
    exit_code = test_status.wait()
    output_gff = ""

    with open("output.gff") as outgff:
        for line in outgff:
            output_gff+=line
    if output_gff == output.decode('UTF-8'):
        print("The test was successful")
    else:
        print("The output is different than expected. Please check")

test_entrypoint()
test_output()
