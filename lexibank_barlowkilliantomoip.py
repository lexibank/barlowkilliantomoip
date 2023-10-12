from pathlib import Path

import attr
import pylexibank
from clldutils.misc import slug


@attr.s
class CustomLexeme(pylexibank.Lexeme):
    Inflected_Forms = attr.ib(default=None)


class Dataset(pylexibank.Dataset):
    dir = Path(__file__).parent
    id = "barlowkilliantomoip"
    form_spec = pylexibank.FormSpec(
        brackets={"(": ")"},
        separators=";/,",
        missing_data=("?", "-"),
        strip_inside_brackets=False,
    )

    lexeme_class = CustomLexeme

    def cmd_download(self, args):
        pass

    def cmd_makecldf(self, args):
        data = self.raw_dir.read_csv("BarlowKillian2023.csv", dicts=True)
        concept_lookup = args.writer.add_concepts(
            id_factory=lambda x: f"{x.number}_{slug(x.english)}", lookup_factory="Name"
        )
        args.writer.add_languages()
        args.writer.add_sources()

        for row in pylexibank.progressbar(data):
            try:
                _ = args.writer.add_forms_from_value(
                    Language_ID=row["Language_ID"],
                    Parameter_ID=concept_lookup[row["English_Gloss"]],
                    Value=row["Form"],
                    Inflected_Forms=row["Inflected_Forms"],
                    Comment=row["Comment"],
                    Source=[row["Source"]],
                )
            except KeyError:
                print(row["English_Gloss"])
