from collections import Counter
from types import SimpleNamespace

from hits import sam, variants


def mapping(qname, cigar, unmapped=False):
    return SimpleNamespace(qname=qname, cigar=cigar, is_unmapped=unmapped,
                           tid=0, seq=None)


def test_count_pe_mismatches_skips_unmapped_and_indel_pairs():
    # 50M2I50M: insertion more than 10 reference bases from either edge
    indel_cigar = [(sam.BAM_CMATCH, 50), (sam.BAM_CINS, 2), (sam.BAM_CMATCH, 50)]
    mappings = iter([
        mapping('r1', [], unmapped=True), mapping('r1', [], unmapped=True),
        mapping('r2', indel_cigar), mapping('r2', [(sam.BAM_CMATCH, 100)]),
    ])
    info = variants.count_pe_mismatches(None, mappings, 100, set())
    assert info['num_reads_skipped'] == 2
    assert info['indel_qnames'] == Counter({'r2': 1})
    assert list(info['mismatches_per_read']) == [0]
