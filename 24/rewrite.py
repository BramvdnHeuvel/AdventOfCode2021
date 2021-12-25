from typing import List
from functools import cache

# model_number      = "11111295969999"

def calculate(model_number : str) -> int:
    """
        >>> calculate("11111295939999")
        4111969752
        >>> calculate("11111295949999")
        158152690
        >>> calculate("11111295959999")
        4111969804
        >>> calculate("11111295969999")
        4111969830

        >>> calculate("99999812449999")
        6682147466
        >>> calculate("99999812439999")
        6682147440
        >>> calculate("99999812429999")
        6682147414
        >>> calculate("99999812419999")
        6682147388
        >>> calculate("99999812399999")
        6682147596
        >>> calculate("99999812389999")
        6682147570
        >>> calculate("99999812379999")
        6682147544

        >>> calculate('14121235622155')
        4147613850
        >>> calculate('51532666444426')
        5349481063
        >>> calculate('21416113112263')
        4422343602
        >>> calculate('43253253563443')
        7489601
        >>> calculate('41223656532335')
        5039211908
        >>> calculate('31535516264214')
        4731701613
        >>> calculate('41541541363466')
        193877207
        >>> calculate('33144361543363')
        182831442
        >>> calculate('36614124411655')
        4791545060
        >>> calculate('56355513416111')
        5408025960
        >>> calculate('61356326645466')
        5657551163
        >>> calculate('54665562314514')
        5385634139
        >>> calculate('36266536254321')
        184221350
        >>> calculate('52434411565234')
        5360939313
        >>> calculate('55244352621616')
        5395668711
        >>> calculate('12522436566213')
        4125698032
        >>> calculate('24516314442613')
        4458446136
        >>> calculate('46344656614362')
        7543029
        >>> calculate('62233143656443')
        218035442
        >>> calculate('66625141262323')
        5718310092
        >>> calculate('45166211551451')
        5086330508
        >>> calculate('25211432542544')
        4468869381
        >>> calculate('36212631142246')
        184218467
        >>> calculate('16451313641332')
        160490317
        >>> calculate('44336351135651')
        5075363708
        >>> calculate('12665336445141')
        158700268
        >>> calculate('24435326365434')
        4457971637
        >>> calculate('12155111533341')
        4123920748
        >>> calculate('12312346215264')
        4124783275
        >>> calculate('52231312636114')
        5359971879
        >>> calculate('11411336113466')
        4113341301
        >>> calculate('62246346462554')
        218037523
        >>> calculate('36665452114256')
        7088113
        >>> calculate('51245663426331')
        5348162806
        >>> calculate('26434261625522')
        4481716031
        >>> calculate('43424254244616')
        5063903511
        >>> calculate('43144166433341')
        5062531876
        >>> calculate('33264631235522')
        182848861
        >>> calculate('26111225342654')
        172318939
        >>> calculate('15321662551161')
        4160411956
        >>> calculate('51666215135445')
        5350005612
        >>> calculate('54461161454626')
        5384647285
        >>> calculate('36231451541636')
        4789666535
        >>> calculate('36223412613311')
        184219294
        >>> calculate('42341341155636')
        194297653
        >>> calculate('43545334512325')
        5064378660
        >>> calculate('63514151213242')
        5682191281
        >>> calculate('53614616326136')
        5373735891
        >>> calculate('41545135242433')
        5040614632
        >>> calculate('66211114221632')
        219861991
        >>> calculate('64362945193462')
        5693129169
    """
    standard_severity = [14, 15, 12, 11, -5, 14, 15, -13, -16, -8, 15, -8, 0, -4]
    error_penalty     = [12,  7,  1,  2,  4, 15, 11,   5,   3,  9,  2,  3, 3, 11]

    severity = 0

    for i in range(14):
        mod_num = int(model_number[i])
        std_sev = standard_severity[i]
        err_pen = error_penalty[i]

        # How badly should this error be fixed?
        rel_sev = (severity % 26) + std_sev

        # This is a nice error. They'll make things less bad.
        if std_sev <= 0:
            severity = severity // 26

        if mod_num == rel_sev:
            # Right model number. (:
            continue
        else:
            # Wrong model number! D: That's a fault.
            severity = 26 * severity + mod_num + err_pen

    return severity

def iterate(standard_severity : List[int], error_penalty : List[int], 
            severity : int = 0, i : int = 0, mod_so_far : str = '') -> List[str]:
    """
        >>> [i for i in iterate( 
        ...     [14, 15, 12, 11, -5, 14, 15, -13, -16, -8, 15, -8, 0, -4], 
        ...     [12,  7,  1,  2,  4, 15, 11,   5,   3,  9,  2,  3, 3, 11],
        ...     26**15, 0
        ... )]
        []
    """
    r = 14 - i
    if not -26**r < severity < 26**r:
        return
    
    s, e = standard_severity[i], error_penalty[i]

    for m in range(1, 10):        
        rel_sev  = (severity % 26) + s
        temp_sev = severity if s > 0 else severity // 26

        if m == rel_sev:
            if i == 13:
                yield mod_so_far + str(m)
            else:
                yield from iterate(standard_severity, error_penalty,
                                severity=temp_sev,
                                i=i+1,
                                mod_so_far=mod_so_far+str(m)
                                )
        else:
            if i == 13:
                pass
            else:
                yield from iterate(
                                    standard_severity, error_penalty,
                                    severity=(26*temp_sev+m+e),
                                    i=i+1,
                                    mod_so_far=mod_so_far+str(m)
                                )





if __name__ == '__main__':
    import doctest

    doctest.testmod()

    for v in iterate([14, 15, 12, 11, -5, 14, 15, -13, -16, -8, 15, -8, 0, -4], 
                     [12,  7,  1,  2,  4, 15, 11,   5,   3,  9,  2,  3, 3, 11]):
        print(v)
