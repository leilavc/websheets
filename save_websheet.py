import config, json, sys
import random

def gen_for(i=-1, n=-1):
    # sharing, attempts_untiL_ref, description, source_code, lang
    definition = {}
    definition['sharing'] = 'visible'
    definition['attempts_until_ref'] = '1'
    definition['lang']  = 'Java'

    # now we need to generate the name, the problem and the answer
    # the problem is: 
    #     write a for loop that prints every i numbers up to n.
    if i == -1:
        i = random.randint(1, 10)

    if n == -1:
        n = random.randint(10, 100)

    name = "gen_for/g%s_%s" % (i, n)
    description = "Write a for loop that prints every %s numbers up to and including %s." % (i, n)
    source_code = "\npublic static void main(String[] args) {\n   for (int i = 0; \[ i <= %s ]\; \[ i += %s]\) {\n      System.out.println(i);\n   }    \n}\n" % (n, i)
    definition['tests'] = "testMain("");"
    definition['description'] = description
    definition['source_code'] = source_code
    return (name, definition)

def save_websheet(problem, definition):
    db = config.connect()
    cursor = db.cursor()

    def done(**response):
        cursor.close()
        db.commit()
        db.close()
        print(json.dumps(response))
        sys.exit(0)

    action = 'save'
    cursor.execute("insert into ws_sheets (author, problem, definition, action, sharing)" +
                   " VALUES (%s, %s, %s, %s, %s)",
                   ('leila', problem, definition, action, 'visible'))

    done(success=True, message=action + " of " + problem + " successful.")
