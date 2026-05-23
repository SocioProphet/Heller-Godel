from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
FND001 = ROOT / "docs" / "framework-foundations" / "HG-FND-001-restricted-proof-grammar.md"
DISTANCE = ROOT / "docs" / "framework-core" / "distance-classification.md"
CLAIM_GRAMMAR = ROOT / "docs" / "framework-core" / "claim-grammar.md"
ANTISEED = ROOT / "docs" / "framework-core" / "anti-seed-framework.md"
P3A = ROOT / "docs" / "gate-minimality" / "p3a-proof-grammar-p3-closure.md"
P3_ASSEMBLY = ROOT / "docs" / "gate-minimality" / "p3-pipeline-integration-closure.md"
A2 = ROOT / "docs" / "gate-minimality" / "a2-minimality-candidate-theorem.md"


class TestHGFND001Normalization(unittest.TestCase):
    def test_normalized_document_exists_and_defines_required_objects(self) -> None:
        self.assertTrue(FND001.exists())
        text = FND001.read_text(encoding="utf-8")
        for token in [
            "HG-FND-001 — Restricted Proof Grammar and Declared Statistics",
            "framework-foundational / Tier 1",
            "simply typed implicational lambda fragment",
            "eta-long beta-normal",
            "de Bruijn",
            "restricted production rules",
            "sigma_C(s)=#lambda-nodes + #application-nodes + #variable-leaves",
            "kappa_r(s)=#constructor-nodes",
            "sigma_C(T)=3 + (2r-1)n",
            "T_r^sigma_C(y)=y^3 C_r(y^(2r-1))",
            "T_2^sigma_C(y)=y^3 C_2(y^3)",
            "T_3^sigma_C(y)=y^3 C_3(y^5)",
            "A-HG-FND-005",
        ]:
            self.assertIn(token, text)

    def test_distance_classification_marks_hg_fnd_001_normalized(self) -> None:
        text = DISTANCE.read_text(encoding="utf-8")
        self.assertIn("`HG-FND-001` | Restricted proof grammar and declared statistics | normalized Tier 1", text)
        self.assertNotIn("`HG-FND-001` | Restricted proof grammar and canonical statistic | candidate", text)

    def test_antiseed_uses_correct_next_fnd_identifier(self) -> None:
        text = ANTISEED.read_text(encoding="utf-8")
        self.assertIn("A-HG-FND-005 — Treating untyped tree analogies as typed proof grammars", text)
        self.assertIn("Status: active; governs `HG-FND-001`.", text)
        self.assertNotIn("A-HG-FND-009 — Treating untyped tree analogies as typed proof grammars", text)

    def test_claim_grammar_and_gate_docs_use_five_surface_chain(self) -> None:
        claim = CLAIM_GRAMMAR.read_text(encoding="utf-8")
        p3a = P3A.read_text(encoding="utf-8")
        p3_assembly = P3_ASSEMBLY.read_text(encoding="utf-8")
        a2 = A2.read_text(encoding="utf-8")

        self.assertIn("`HG-FND-001` | Restricted proof grammar and declared statistics | framework-foundational / normalized Tier 1", claim)
        self.assertIn("method-grade modulo five remaining candidate Tier-1 surfaces", claim)
        self.assertIn("method-grade with normalized `HG-FND-001` dependency", p3a)
        self.assertIn("normalized `HG-FND-001`", p3_assembly)
        self.assertIn("method-grade modulo five remaining candidate Tier-1 surfaces", a2)

        active_text = "\n".join([claim, p3a, p3_assembly, a2])
        self.assertNotIn("method-grade modulo six candidate Tier-1 surfaces", active_text)
        self.assertNotIn("method-grade modulo candidate-`HG-FND-001`", active_text)
        self.assertNotIn("candidate-`HG-FND-001` grade ceiling", active_text)

    def test_remaining_candidate_surfaces_are_explicit(self) -> None:
        for path in [CLAIM_GRAMMAR, P3_ASSEMBLY, A2]:
            text = path.read_text(encoding="utf-8")
            for token in [
                "HG-FND-002",
                "HG-FND-003",
                "HG-VOC-006",
                "HG-FND-006",
                "HG-FND-007",
            ]:
                self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
